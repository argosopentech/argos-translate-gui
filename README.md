# Argos Translate GUI

[Website](https://www.argosopentech.com) | [GitHub](https://github.com/argosopentech/argos-translate-gui) | [PyPI](https://pypi.org/project/argostranslategui/)

Graphical user interface for [Argos Translate](https://github.com/argosopentech/argos-translate).

![Screenshot](/img/Screenshot.png)
![Screenshot2](/img/Screenshot2.png)

## Install
```
pip3 install argostranslategui


```

### Build and install snap package
1. Install [snapd](https://snapcraft.io/docs/installing-snapd) if it isn't already installed.
2. Using snapd install snapcraft and its dependency multipass:
```
sudo snap install multipass
sudo snap install snapcraft
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

