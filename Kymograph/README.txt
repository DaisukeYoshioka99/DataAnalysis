
This ImageJ macro extracts the cell contour in the confocal fluorescence microscope image and creates a fluorescence kymograph on the cell membrane.
Expected run time for demo on a "normal" desktop computer is about 30 sec.

We has been tested on the following software.

Fiji (ver. 1.50e)


1. Open Fiji.

2. Plugins -> Macros -> Install… -> RoundCellDetection.ijm.

3. Open “Data.tif”.

4. Plugins -> Macros -> RoundCellDetection.

5. If the cells are not fixed, remove the ROI. If the position of the circle is misaligned, manually fine-adjust the position of the circle so as to follow the cell contour. This operation is important for improving the reproducibility of quantitative results.

6. Plugins -> Macros -> Install… -> Kymograph.ijm.

7. Plugins -> Macros -> Kymograph.
The left half of the image shows the fluorescence of the cell membrane and the right half shows the fluorescence of the cytoplasm.

8. Save “Kymograph.tif”.
