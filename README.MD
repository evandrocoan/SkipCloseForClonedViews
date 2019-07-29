# Skip Close For Cloned Views

This implements the issue:
1. https://github.com/SublimeTextIssues/Core/issues/2903 Skip save (ask) when closing a cloned view

Sometimes I just open a clone view to peek somewhere else,
then I close it because I do not need it.
But if the buffer was already dirty,
when I close the clone view,
Sublime Text keeps asking whether I would like to save my changes.

(You can clone a view by going on the menu `File -> New view into file`)

There there is a setting called `skip_close_for_cloned_views` where you can set in any settings hierarchy:
Settings files are consulted in this order:
1. Packages/Default/Preferences.sublime-settings
2. Packages/Default/Preferences (`<platform>`).sublime-settings
3. Packages/User/Preferences.sublime-settings **<--we are around here, the 3º less priority level**
4. `<Project Settings>`
5. `Packages/<syntax>/<syntax>.sublime-settings`
6. `Packages/User/<syntax>.sublime-settings`
7. `<Buffer Specific Settings>`

See a more detailed discussion about settings loading ordering here:
1. https://github.com/TheSpyder/SyncedSideBar/pull/41#issuecomment-249726691


___
## License

All files in this repository are released under GNU General Public License v3.0
or the latest version available on http://www.gnu.org/licenses/gpl.html

1. The [LICENSE](LICENSE) file for the GPL v3.0 license
1. The website https://www.gnu.org/licenses/gpl-3.0.en.html

For more information.


