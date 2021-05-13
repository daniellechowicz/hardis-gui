# HARDIS GUI
 GUI application for automatic analysis of cutting forces

## Installation (tested on 64-bit version of Windows)
1) download the contents of the repository (green button in the upper right corner)
2) go to _installer_ folder and double click on _python-3.9.0-amd64.exe_ file
3) follow the instructions - however, make sure that <i>Add Python 3.9 to PATH</i> is checked (see below)
5) open the folder and double click on <i>setup.bat</i>
6) when the installation of the modules is finished, go to the _bin_ folder and run the application (<i>HARDIS.exe</i> - if this fails, run <i>HARDIS3.exe</i>)

## Manual

### Main view
After launching the application, you will see the main view of the application. In the main view, enter the required parameters, i.e. the column number corresponding to the cutting forces (numbering starts from 0), the index of the cutting speed in the file name (numbering starts from 0) and the used sampling rate in Hz. After completing the steps described above, you have two options to choose from: single or batch analysis.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/hardis-gui/blob/main/img/main.png">
</p>

### Single analysis
Single analysis is used to analyze files one by one. Use it when you notice that an error was present during batch analysis.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/hardis-gui/blob/main/img/single.png">
</p>

### Batch analysis
Batch analysis enables automated analysis of all files. However, it is important that the way the files are named remains the same. The cutting speed index in the file name must not be changed - otherwise errors will occur. Once you have approved the path to the measurement data folder, be patient and do not press anything. To track progress, go to the _data_ folder (level above), and then open the _figures_ folder. In this folder the results of the analysis will be saved as graphs - this way you can check if the results are correct (the force range taken for the analysis is marked with blue asterisks, as shown in the legend). The data are saved in CSV format in the _data_ folder.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/hardis-gui/blob/main/img/figure.png">
</p>
