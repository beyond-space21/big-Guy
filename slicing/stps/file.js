
    function getdata(file) {
        var txt = readTextFile(file);
        if (txt != '!') {
           return extract(txt)
        } else {
           return '!'
        }
    }

    var points = []
    var normals = []
    function readTextFile(file) {
        var rawFile = new XMLHttpRequest();
        var data;
        rawFile.open("GET", file, false);
        rawFile.onreadystatechange = function () {
            if (rawFile.readyState === 4) {
                if (rawFile.status === 200 || rawFile.status == 0) {
                    data = rawFile.responseText;
                } else {
                    data = 'err'
                }
            }
        }
        rawFile.send(null);
        return data;
    }
    function extract(file) {
        var totalTriangles = 0
        var pointer = 0
        var line = 0

        for (var i = 0; line != 10; i++) {//to skip to the start of actual data
            if (file[i] === '\n') {
                line++
            }
            if (file[i] === ':') {//to read number of total triangles
                var s = ''      //if dynamic metadata to be read, json need to be implemented on both write and read functions
                for (var e = 1; file[i + e + 1] != '\n'; e++) {
                    s = s.concat(file[i + e])
                }
                totalTriangles = parseInt(s)
            }
            pointer = i + 1
        }

        for (var i = 0; i < totalTriangles; i++) { //looped for total number of triangles
            var chips = []
            for (var dataline = 0; dataline < 4; dataline++) { //looped for total number of data for eacd triangle
                snip = ''
                for (pointer; file[pointer] != '\n' && file[pointer]; pointer++) { //looped for each cordinate on one line
                    if (file[pointer] != ' ') {
                        snip = snip.concat(file[pointer])
                    } else {
                        chips.push(parseFloat(snip))
                        snip = ''
                    }
                }
                chips.push(parseFloat(snip))
                if (dataline == 0) { //save first line data as normals
                    normals.push(chips)
                    chips = []
                }
                pointer = pointer + 1
            }
            points.push(chips) //save other data as points
            pointer = pointer + 2
        }

        return {normals:normals,points:points}
    }