function files_request(){
    let requestOptions = {
		method: 'POST',
		headers: {
			"X-CSRFToken": getCookie('csrftoken'),
		},
		body: JSON.stringify({
            action: 'request_files',
        })
	}
	
	fetch('./', requestOptions)
		.then(response => {
			if (response.ok) {
				show_files(response)
			}
            else{
                throw new Error('Network response was not ok.');

            }
		})

		.then(response => {
			console.log(response)
		})

		.catch(error => {
			console.error('There was a problem with the fetch operation:', error);
		})
}

function show_files(){
    console.log(response)
}