# Skip Close For Cloned Views

This implements the issue:
1. https://github.com/SublimeTextIssues/Core/issues/2903 Skip save (ask) when closing a cloned view

Sometimes I just open a clone view to peek somewhere else,
then I close it because I do not need it.
But if the buffer was already dirty,
when I close the clone view,
Sublime Text keeps asking whether I would like to save my changes.

(You can clone a view by going on the menu `File -> New view into file`)

There there is a setting called `skip_close_for_cloned_views`:
```js
    // Enable or disable the save question for views from cloned files (default true)
    "skip_close_for_cloned_views": true,
```

You can set the setting `skip_close_for_cloned_views` in any settings hierarchy.
The settings files are consulted in this order:
1. Packages/Default/Preferences.sublime-settings
2. Packages/Default/Preferences (`<platform>`).sublime-settings
3. Packages/User/Preferences.sublime-settings **<--we are around here, the 3º less priority level**
4. `<Project Settings>`
5. `Packages/<syntax>/<syntax>.sublime-settings`
6. `Packages/User/<syntax>.sublime-settings`
7. `<Buffer Specific Settings>`

See a more detailed discussion about settings loading ordering here:
1. https://github.com/TheSpyder/SyncedSideBar/pull/41#issuecomment-249726691


## Installation

### By Package Control

1. Download & Install **`Sublime Text 3`** (https://www.sublimetext.com/3)
1. Go to the menu **`Tools -> Install Package Control`**, then,
   wait few seconds until the installation finishes up
1. Now,
   Go to the menu **`Preferences -> Package Control`**
1. Type **`Add Channel`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
   input the following address and press <kbd>Enter</kbd>
   ```
   https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json
   ```
1. Go to the menu **`Tools -> Command Palette...
   (Ctrl+Shift+P)`**
1. Type **`Preferences:
   Package Control Settings – User`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
   find the following setting on your **`Package Control.sublime-settings`** file:
   ```js
       "channels":
       [
           "https://packagecontrol.io/channel_v3.json",
           "https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json",
       ],
   ```
1. And,
   change it to the following, i.e.,
   put the **`https://raw.githubusercontent...`** line as first:
   ```js
       "channels":
       [
           "https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json",
           "https://packagecontrol.io/channel_v3.json",
       ],
   ```
   * The **`https://raw.githubusercontent...`** line must to be added before the **`https://packagecontrol.io...`** one, otherwise,
     you will not install this forked version of the package,
     but the original available on the Package Control default channel **`https://packagecontrol.io...`**
1. Now,
   go to the menu **`Preferences -> Package Control`**
1. Type **`Install Package`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
search for **`SkipCloseForClonedViews`** and press <kbd>Enter</kbd>

See also:
1. [ITE - Integrated Toolset Environment](https://github.com/evandrocoan/ITE)
1. [Package control docs](https://packagecontrol.io/docs/usage) for details.


___
## License

All files in this repository are released under GNU General Public License v3.0
or the latest version available on http://www.gnu.org/licenses/gpl.html

1. The [LICENSE](LICENSE) file for the GPL v3.0 license
1. The website https://www.gnu.org/licenses/gpl-3.0.en.html

For more information.


