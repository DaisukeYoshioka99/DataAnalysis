
//Detect cell contour for kimograph drawing.
macro "RoundCellDetection"{

	run("Duplicate...", "duplicate");
	id=getImageID();
	run("ROI Manager...");//Leave the ROI manager open.
	setBatchMode(true);
	
	run("Z Project...", "projection=[Average Intensity]");
	run("Gaussian Blur...", "sigma=1");
	
	setAutoThreshold("Li dark");
	//run("Threshold...");
	setOption("BlackBackground", false);
	run("Convert to Mask");
	run("Fill Holes");
	run("Watershed");
	run("Analyze Particles...", "size=70-Infinity circularity=0.80-1.00 clear add"); 
	
	close();
	
	n = roiManager("count");
	for (i=0; i<n; i++) {
		roiManager("select", 0);
		run("Fit Circle");
		roiManager("Add")
		roiManager("select", 0);
		roiManager("Delete");
	}
	
	n = roiManager("count");
	for (i=0; i<n; i++) {
		//Select ROI one by one.
		roiManager("select", i);
		//Get size of ROI.
		Roi.getBounds(x,y,w,h);
		//Calculate radius of ROI.
		r = w/2;
		dw=round(0.1*w);
		dh=round(0.1*h);
		//Create a small ROI.
		makeOval(x+dw, y+dh, w-2*dw, h-2*dh);
		roiManager("Update");
	}
	
	setBatchMode(false);
	selectImage(id);
	roiManager("Show All");

}


