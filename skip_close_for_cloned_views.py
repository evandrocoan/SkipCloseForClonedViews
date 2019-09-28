import sublime
import sublime_plugin


class SkipCloseForClonedViewsEventListener(sublime_plugin.EventListener):
    closed_view = None
    cloned_buffers_ids = {}

    @classmethod
    def is_cloned(cls, input_view):
        buffer_id = input_view.buffer_id()
        return \
            len( [
                    view
                        for window in sublime.windows()
                            for view in window.views()
                                if view.buffer_id() == buffer_id
                ] ) > 1

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

