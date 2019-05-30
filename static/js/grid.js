function setPixelColor(id) {
	if (document.getElementById(id).style.backgroundColor == 'black') {
			document.getElementById(id).style.backgroundColor = 'white';
			document.getElementById(id).setAttribute("value", 0)
	}
	else {
			document.getElementById(id).style.backgroundColor = 'black';
			document.getElementById(id).setAttribute("value", 1)
	}
}

function showValues() {
	var output = ""
	for (var i = 0; i < 19; i++) {
			for (var j = 0; j < 19; j++) {
					output = output + document.getElementById("pixel-" + i + "-" + j).getAttribute("value");
					if(!(i==18 && j==18)){
							output = output + ",";
					}
					
			}
	}
	console.log(output)
	document.getElementById("output").innerHTML = output;
}

function savePixelColor() {
	// var output = ""
	var output = [];
	for (var i = 0; i < 19; i++) {
		for (var j = 0; j < 19; j++) {
			// output = output + document.getElementById("pixel-" + i + "-" + j).getAttribute("value");
			var val = document.getElementById("pixel-" + i + "-" + j).getAttribute("value");
			output.push(val);
			if(!(i==18 && j==18)){
				// output = output + ",";
			}		
		}
	}
	if (objCounter <= 5) {
			name1Objs.push(output);
	}
	else if(objCounter < 10) {
		name2Objs.push(output);
	}
	else {
		name2Objs.push(output);
		document.getElementById("name1Objs").value = JSON.stringify(name1Objs);
		document.getElementById("name2Objs").value = JSON.stringify(name2Objs);
		document.getElementById("regForm").submit();
		console.log(name1Objs);
		console.log(name2Objs);
	}
	document.getElementById("counter").innerHTML = objCounter++;
}

function resetPixelColor() {
	var els = document.getElementsByClassName("pixel")
	Array.prototype.forEach.call(els, function(el) {
		el.style.backgroundColor = 'white';
		el.setAttribute("value", 0);
	});
}

function tableCreate() {
	var artContainer = document.getElementById('artContainer');
	var artDiv = document.createElement('div');
	artDiv.setAttribute('class', 'art');
	for (var i = 0; i < 19; i++) {
			var div = document.createElement('div');
			div.setAttribute('class', 'row');
			for (var j = 0; j < 19; j++) {
					var colDiv = document.createElement('div');
					colDiv.setAttribute('class', 'pixel');
					colDiv.id = "pixel-" + i + "-" + j;
					colDiv.setAttribute("value", 0)
					colDiv.setAttribute("onclick", "setPixelColor(this.id)");
					div.appendChild(colDiv);
			}
			artDiv.appendChild(div);
	}
artContainer.appendChild(artDiv);
}