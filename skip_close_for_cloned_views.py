import sublime
import sublime_plugin


class SkipCloseForClonedViewsEventListener(sublime_plugin.EventListener):
    closed_view = None
    cloned_buffers_ids = {}

    def on_load(self, view):
        # print('on_load', view.buffer_id())
        self.on_new( view )

    def on_new(self, view):
        # print('on_new', view.buffer_id())
        buffer_id = view.buffer_id()
        self.cloned_buffers_ids[buffer_id] = 1

    def on_clone(self, view):
        # print('on_clone', view.buffer_id())
        buffer_id = view.buffer_id()

        if buffer_id not in self.cloned_buffers_ids:
            self.create_cloned_buffers()

        else:
            self.cloned_buffers_ids[buffer_id] += 1

        # print('cloned_buffers_ids   ', self.cloned_buffers_ids)

    def on_close(self, view):
        # print('on_close', view.buffer_id())
        buffer_id = view.buffer_id()

        if buffer_id not in self.cloned_buffers_ids:
            self.create_cloned_buffers()

        else:
            self.cloned_buffers_ids[buffer_id] -= 1

        # print('cloned_buffers_ids   ', self.cloned_buffers_ids)
        if buffer_id in self.cloned_buffers_ids and self.cloned_buffers_ids[buffer_id] < 1:
            del self.cloned_buffers_ids[buffer_id]

    @classmethod
    def create_cloned_buffers(cls):
        """ Fix our internal buffers when Sublime Text is started with several views
        https://github.com/SublimeTextIssues/Core/issues/5
        """
        windows = sublime.windows()

        for window in windows:
            views = window.views()

            for view in views:
                buffer_id = view.buffer_id()

                if buffer_id in cls.cloned_buffers_ids:
                    cls.cloned_buffers_ids[buffer_id] += 1

                else:
                    cls.cloned_buffers_ids[buffer_id] = 1

        # print('create_cloned_buffers', cls.cloned_buffers_ids)

    @classmethod
    def is_cloned(cls, view):
        buffer_id = view.buffer_id()
        if buffer_id not in cls.cloned_buffers_ids: cls.create_cloned_buffers()

        return cls.cloned_buffers_ids[buffer_id] > 1

    def on_window_command(self, window, command_name, args):
        # print('window', window, command_name, args)

        if command_name == "close":
            view = window.active_view()
            if view.is_scratch(): return

            skip_close_for_cloned_views = view.settings().get("skip_close_for_cloned_views", True)
            # print('skip_close_for_cloned_views', skip_close_for_cloned_views)

            if skip_close_for_cloned_views and self.is_cloned( view ):
                view.set_scratch( True )
                self.closed_view = view

    def on_post_window_command(self, window, command_name, args):
        # print('window', window, command_name, args)
        view = self.closed_view

        if command_name == "close" and view:
            self.closed_view = None
            view.set_scratch( False )

