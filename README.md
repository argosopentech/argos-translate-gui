# Argos Translate GUI

[Website](https://www.argosopentech.com) | [GitHub](https://github.com/argosopentech/argos-translate-gui) | [PyPI](https://pypi.org/project/argostranslategui/)

Graphical user interface for [Argos Translate](https://github.com/argosopentech/argos-translate).

![Screenshot](/img/Screenshot.png)
![Screenshot2](/img/Screenshot2.png)

## Install
```
pip3 install argostranslategui


```

## Snapcraft

### Build and install snap package
1. Install [snapd](https://snapcraft.io/docs/installing-snapd) if it isn't already installed.
2. Using snapd install snapcraft and its dependency multipass:
```
sudo snap install multipass
sudo snap install --classic snapcraft
```
3. Clone this repo:
```
git clone https://github.com/argosopentech/argos-translate-gui.git
```
4. From the root directory of this project build the snap package:
```
cd argos-translate-gui
SNAPCRAFT_BUILD_ENVIRONMENT_MEMORY=4G snapcraft
```
Any *unzipped* package files in package/ will be automatically included in the snap archive (and won't be able to be deleted by users of the snap).

Note, the build won't run with Snapcraft's default build memory of 2GB so you need to set the SNAPCRAFT_BUILD_ENVIRONMENT environment variable. [More on Snapcraft forum](https://forum.snapcraft.io/t/snapcraft-configuration-of-multipass-vm-arguments/9761).

5. Install the snap package:
```
sudo snap install --devmode argos-translate_<version information>.snap
```

### Install from Snap Store
* Snap store install [currently unavailable](https://forum.snapcraft.io/t/omp-permission-error/28425) but snap build and install can still be done manually.

Argos Translate is available from the Snap Store and auto installs a content snap to support translation between Arabic, Chinese, English, French, Russian, and Spanish. Additional languages can be installed from supplementary content snaps.

With [snapd installed](https://snapcraft.io/docs/installing-snapd):
```
sudo snap install argos-translate
```
[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-white.svg)](https://snapcraft.io/argos-translate)

Automatically installs and connects to `argos-translate-base-langs` snap to support translations between Arabic, Chinese, English, French, Russian, and Spanish.

Additional languages can be installed from *.argosmodel files or from supplementary content snaps:
* argos-translate-de-en - German - English
* argos-translate-en-it - English - Italian
* argos-translate-en-pt - English - Portuguese

To connect automatically:
`sudo snap connect argos-translate:argos-packages argos-translate-en-it:argos-packages`

To run command line interface on Snapcraft:
```
argos-translate.cli --help
```
