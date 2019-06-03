if (window.addEventListener) {							
		window.addEventListener("resize", browserResize);
} else if (window.attachEvent) {								 
		window.attachEvent("onresize", browserResize);
}
var xbeforeResize = window.innerWidth;

function browserResize() {
		var afterResize = window.innerWidth;
		if ((xbeforeResize < (970) && afterResize >= (970)) || (xbeforeResize >= (970) && afterResize < (970)) ||
				(xbeforeResize < (728) && afterResize >= (728)) || (xbeforeResize >= (728) && afterResize < (728)) ||
				(xbeforeResize < (468) && afterResize >= (468)) ||(xbeforeResize >= (468) && afterResize < (468))) {
				xbeforeResize = afterResize;
				 
		}
		fixDragBtn();
		showFrameSize();
}
var fileID = "";
var loadSave = false;
function getSavedFile() {
		loadSave = true;
		var htmlCode;
		var paramObj = {};
		paramObj.fileid = "";
		fileID = paramObj.fileid;
		var paramA = JSON.stringify(paramObj);
		var httpA = new XMLHttpRequest();
		httpA.open("POST", globalURL, true);
		httpA.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		httpA.onreadystatechange = function() {
				if(httpA.readyState == 4 && httpA.status == 200) {
						document.getElementById("textareaCode").value = httpA.responseText;
						window.editor.getDoc().setValue(httpA.responseText);
						loadSave = false;
				}
		}
		httpA.send(paramA);	 
}

function retheme() {
	var cc = document.body.className;
	if (cc.indexOf("darktheme") > -1) {
		document.body.className = cc.replace("darktheme", "");
	} else {
		document.body.className += " darktheme";
	}
}

function showFrameSize() {
	var t;
	var width, height;
	width = Number(w3_getStyleValue(document.getElementById("iframeResult"), "width").replace("px", "")).toFixed();
	height = Number(w3_getStyleValue(document.getElementById("iframeResult"), "height").replace("px", "")).toFixed();
	document.getElementById("framesize").innerHTML = "Result Size: <span>" + width + " x " + height + "</span>";
}
var dragging = false;
var stack;
function fixDragBtn() {
	var textareawidth, leftpadding, dragleft, containertop, buttonwidth
	var containertop = Number(w3_getStyleValue(document.getElementById("container"), "top").replace("px", ""));
	if (stack != " horizontal") {
	document.getElementById("dragbar").style.width = "5px";	
	textareasize = Number(w3_getStyleValue(document.getElementById("textareawrapper"), "width").replace("px", ""));
	leftpadding = Number(w3_getStyleValue(document.getElementById("textarea"), "padding-left").replace("px", ""));
	buttonwidth = Number(w3_getStyleValue(document.getElementById("dragbar"), "width").replace("px", ""));
	textareaheight = w3_getStyleValue(document.getElementById("textareawrapper"), "height");
	dragleft = textareasize + leftpadding + (leftpadding / 2) - (buttonwidth / 2);
	document.getElementById("dragbar").style.top = containertop + "px";
	document.getElementById("dragbar").style.left = dragleft + "px";
	document.getElementById("dragbar").style.height = textareaheight;
	document.getElementById("dragbar").style.cursor = "col-resize";
	
	} else {
	document.getElementById("dragbar").style.height = "5px";
	if (window.getComputedStyle) {
		textareawidth = window.getComputedStyle(document.getElementById("textareawrapper"),null).getPropertyValue("height");
		textareaheight = window.getComputedStyle(document.getElementById("textareawrapper"),null).getPropertyValue("width");
		leftpadding = window.getComputedStyle(document.getElementById("textarea"),null).getPropertyValue("padding-top");
		buttonwidth = window.getComputedStyle(document.getElementById("dragbar"),null).getPropertyValue("height");
	} else {
		dragleft = document.getElementById("textareawrapper").currentStyle["width"];
	}
	textareawidth = Number(textareawidth.replace("px", ""));
	leftpadding = Number(leftpadding .replace("px", ""));
	buttonwidth = Number(buttonwidth .replace("px", ""));
	dragleft = containertop + textareawidth + leftpadding + (leftpadding / 2);
	document.getElementById("dragbar").style.top = dragleft + "px";
	document.getElementById("dragbar").style.left = "5px";
	document.getElementById("dragbar").style.width = textareaheight;
	document.getElementById("dragbar").style.cursor = "row-resize";		
	}
}
function dragstart(e) {
	e.preventDefault();
	dragging = true;
	var main = document.getElementById("iframecontainer");
}
function dragmove(e) {
	if (dragging)
	{
	document.getElementById("shield").style.display = "block";
	if (stack != " horizontal") {
		var percentage = (e.pageX / window.innerWidth) * 100;
		if (percentage > 5 && percentage < 98) {
		var mainPercentage = 100-percentage;
		document.getElementById("textareacontainer").style.width = percentage + "%";
		document.getElementById("iframecontainer").style.width = mainPercentage + "%";
		fixDragBtn();
		}
	} else {
		var containertop = Number(w3_getStyleValue(document.getElementById("container"), "top").replace("px", ""));
		var percentage = ((e.pageY - containertop + 20) / (window.innerHeight - containertop + 20)) * 100;
		if (percentage > 5 && percentage < 98) {
		var mainPercentage = 100-percentage;
		document.getElementById("textareacontainer").style.height = percentage + "%";
		document.getElementById("iframecontainer").style.height = mainPercentage + "%";
		fixDragBtn();
		}
	}
	showFrameSize();	
	}
}
function dragend() {
	document.getElementById("shield").style.display = "none";
	dragging = false;
	if (window.editor) {
	window.editor.refresh();
	}
}

function w3_getStyleValue(elmnt,style) {
	if (window.getComputedStyle) {
		return window.getComputedStyle(elmnt,null).getPropertyValue(style);
	} else {
		return elmnt.currentStyle[style];
	}
}

function openMenu() {
	var x = document.getElementById("navbarDropMenu");
	var y = document.getElementById("menuOverlay");
	var z = document.getElementById("menuButton");
	if (z.className.indexOf("w3-text-gray") == -1) {
		z.className += " w3-text-gray";
	} else { 
		z.className = z.className.replace(" w3-text-gray", "");
	}
	if (z.className.indexOf("w3-gray") == -1) {
		z.className += " w3-gray";
	} else { 
		z.className = z.className.replace(" w3-gray", "");
	}
	if (x.className.indexOf("w3-show") == -1) {
		x.className += " w3-show";
	} else { 
		x.className = x.className.replace(" w3-show", "");
	}
	if (y.className.indexOf("w3-show") == -1) {
		y.className += " w3-show";
	} else { 
		y.className = y.className.replace(" w3-show", "");
	}
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
	if (event.target == document.getElementById("menuOverlay")) {
		openMenu();
	}
}