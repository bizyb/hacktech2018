

function transmitAudio(audioBlobObj) {

    var csrftoken = Cookies.get('csrftoken');
    console.log(csrftoken);
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("POST", "audio-post", true);
	xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
	xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xmlhttp.send(audioBlobObj);
}

function voiceAssit() {
	// request permission to access audio stream
	navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
	    // store streaming data chunks in array
	    const chunks = [];
	    // create media recorder instance to initialize recording
	    const recorder = new MediaRecorder(stream);
	    // function to be called when data is received
	    recorder.ondataavailable = e => {
	      // add stream data to chunks
	      chunks.push(e.data);
	      // if recorder is 'inactive' then recording has finished
	      if (recorder.state == 'inactive') {
	          // convert stream data chunks to a 'webm' audio format as a blob
	          const blob = new Blob(chunks, { type: 'audio/x-wav' });
	          // convert blob to URL so it can be assigned to a audio src attribute
	          transmitAudio(blob);
	      }
	    };
	    // start recording with 1 second time between receiving 'ondataavailable' events
	    recorder.start(1000);
	    // setTimeout to stop recording after 15 seconds
	    setTimeout(() => {
	        // this will trigger one final 'ondataavailable' event and set recorder state to 'inactive'
	        recorder.stop();
	    }, 5000);
	  }).catch(console.error);

}
// window.onload = imageTopMargin();
