var currentIndex = 0;
var rows = document.getElementById("myTable").getElementsByTagName('tbody')[0].getElementsByTagName('tr');
var itemsPerPage = 5; // Set the number of items per page
var maxVisiblePages = 2; // Set the maximum number of visible pages before using ellipsis
alert("sam");
function showRows(startIndex) {
  for (var i = 0; i < rows.length; i++) {
    rows[i].style.display = 'none';
  }
  for (var i = startIndex; i < startIndex + itemsPerPage && i < rows.length; i++) {
    rows[i].style.display = 'table-row';
  }
}

function updatePaginationButtons() {
  var totalPages = Math.ceil(rows.length / itemsPerPage);
  var paginationContainer = document.getElementById("pagination");
  paginationContainer.innerHTML = '';

  if (totalPages >= maxVisiblePages) {
    var startPage = Math.max(1, Math.min(totalPages - maxVisiblePages + 1, Math.ceil(currentIndex / itemsPerPage) - Math.floor(maxVisiblePages / 2) + 1));
    var backedpage = Math.max(1, Math.min(totalPages - maxVisiblePages + 1, Math.ceil(currentIndex / itemsPerPage) - Math.floor(maxVisiblePages / 4) + 1));
    var endPage = Math.min(totalPages, backedpage + maxVisiblePages - 1);
    
    if(startPage >= "3"){
      var firstbutton = document.createElement("button");
      firstbutton.innerHTML = "1";
      firstbutton.addEventListener("click", function() {
      currentIndex = (parseInt(this.innerHTML) - 1) * itemsPerPage;
      showRows(currentIndex);
      updatePaginationButtons()
    });
    paginationContainer.appendChild(firstbutton);
    var ellipsis = document.createElement("button");
      ellipsis.innerHTML = "...";
      ellipsis.classList.add("ellipsis");
      ellipsis.disabled = false;
      paginationContainer.appendChild(ellipsis);
    }

        for (var i = startPage; i <= endPage; i++) {
        var button = document.createElement("button");
        button.innerHTML = i;
        button.addEventListener("click", function() {
          currentIndex = (parseInt(this.innerHTML) - 1) * itemsPerPage;
          showRows(currentIndex);
          updatePaginationButtons();
        });  
        if (i === Math.ceil((currentIndex + 2) / itemsPerPage)) {
          button.classList.add("active");
        }  
        paginationContainer.appendChild(button);
      }
      
    if (endPage < totalPages) {
      var ellipsis = document.createElement("button");
      ellipsis.innerHTML = "...";
      ellipsis.classList.add("ellipsis");
      ellipsis.disabled = false;
      paginationContainer.appendChild(ellipsis);
    }
    var lastPageButton = document.createElement("button");
    lastPageButton.innerHTML = totalPages;
    lastPageButton.addEventListener("click", function() {
      currentIndex =  Math.floor((rows.length - 1) / itemsPerPage) * itemsPerPage;
      showRows(currentIndex);
      updatePaginationButtons();
    });
    if (endPage !== totalPages) {
      paginationContainer.appendChild(lastPageButton);
    }   
    
    
  }
   else {
    for (var i = 1; i <= totalPages; i++) {
      var button = document.createElement("button");
      button.innerHTML = i;
      button.addEventListener("click", function() {
        currentIndex =  Math.floor((rows.length - 1) / itemsPerPage) * itemsPerPage;
        showRows(currentIndex);
        updatePaginationButtons();
      });

      if (i === Math.ceil((currentIndex + 1) / itemsPerPage)) {
        button.classList.add("active");
      }
      paginationContainer.appendChild(button);
    }
  }
}

function nextPage() {
    alert{"fgh"};
  currentIndex += itemsPerPage;
  if (currentIndex >= rows.length) {
    currentIndex = 0; // Wrap around to the first row if reaching the end
  }
  showRows(currentIndex);
  updatePaginationButtons();
}

function previousPage() {
  currentIndex -= itemsPerPage;
  if (currentIndex < 0) {
    currentIndex = Math.floor((rows.length - 1) / itemsPerPage) * itemsPerPage; // Wrap around to the last page
  }
  showRows(currentIndex);
  updatePaginationButtons();
}






var videodata = document.getElementById("videotable").getElementsByTagName('tbody')[0].getElementsByTagName('tr');
function showRowsvideo(startIndex) {
  for (var i = 0; i < videodata.length; i++) {
    videodata[i].style.display = 'none';
  }
  for (var i = startIndex; i < startIndex + itemsPerPage && i < videodata.length; i++) {
    videodata[i].style.display = 'table-row';
  }
}

function updatevideoPaginationButtons() {
  var totalPages = Math.ceil(videodata.length / itemsPerPage);
  var paginationContainer = document.getElementById("paginationvideo");
  paginationContainer.innerHTML = '';

  if (totalPages >= maxVisiblePages) {
    var startPage = Math.max(1, Math.min(totalPages - maxVisiblePages + 1, Math.ceil(currentIndex / itemsPerPage) - Math.floor(maxVisiblePages / 2) + 1));
    var backedpage = Math.max(1, Math.min(totalPages - maxVisiblePages + 1, Math.ceil(currentIndex / itemsPerPage) - Math.floor(maxVisiblePages / 4) + 1));
    var endPage = Math.min(totalPages, backedpage + maxVisiblePages - 1);
    
    if(startPage >= "3"){
      var firstbutton = document.createElement("button");
      firstbutton.innerHTML = "1";
      firstbutton.addEventListener("click", function() {
      currentIndex = (parseInt(this.innerHTML) - 1) * itemsPerPage;
      showRowsvideo(currentIndex);
      updatevideoPaginationButtons()
    });
    paginationContainer.appendChild(firstbutton);
    var ellipsis = document.createElement("button");
      ellipsis.innerHTML = "...";
      ellipsis.classList.add("ellipsis");
      ellipsis.disabled = false;
      paginationContainer.appendChild(ellipsis);
    }

        for (var i = startPage; i <= endPage; i++) {
        var button = document.createElement("button");
        button.innerHTML = i;
        button.addEventListener("click", function() {
          currentIndex = (parseInt(this.innerHTML) - 1) * itemsPerPage;
          showRowsvideo(currentIndex);
      updatevideoPaginationButtons()
        });  
        if (i === Math.ceil((currentIndex + 2) / itemsPerPage)) {
          button.classList.add("active");
        }  
        paginationContainer.appendChild(button);
      }
      
    if (endPage < totalPages) {
      var ellipsis = document.createElement("button");
      ellipsis.innerHTML = "...";
      ellipsis.classList.add("ellipsis");
      ellipsis.disabled = false;
      paginationContainer.appendChild(ellipsis);
    }
    var lastPageButton = document.createElement("button");
    lastPageButton.innerHTML = totalPages;
    lastPageButton.addEventListener("click", function() {
      currentIndex =  Math.floor((videodata.length - 1) / itemsPerPage) * itemsPerPage;
      showRowsvideo(currentIndex);
      updatevideoPaginationButtons()
    });
    if (endPage !== totalPages) {
      paginationContainer.appendChild(lastPageButton);
    }   
    
    
  }
   else {
    for (var i = 1; i <= totalPages; i++) {
      var button = document.createElement("button");rows
      button.innerHTML = i;
      button.addEventListener("click", function() {
        currentIndex =  Math.floor((videodata.length - 1) / itemsPerPage) * itemsPerPage;
        showRowsvideo(currentIndex);
      updatevideoPaginationButtons()
      });

      if (i === Math.ceil((currentIndex + 1) / itemsPerPage)) {
        button.classList.add("active");
      }
      paginationContainer.appendChild(button);
    }
  }
}

function nextPagevideo() {
  currentIndex += itemsPerPage;
  if (currentIndex >= videodata.length) {
    currentIndex = 0; // Wrap around to the first row if reaching the end
  }
  showRowsvideo(currentIndex);
      updatevideoPaginationButtons();
}

function previousPagevideo() {
  currentIndex -= itemsPerPage;
  if (currentIndex < 0) {
    currentIndex = Math.floor((videodata.length - 1) / itemsPerPage) * itemsPerPage; // Wrap around to the last page
  }
  showRowsvideo(currentIndex);
      updatevideoPaginationButtons();
}





var audiodata = document.getElementById("audiotable").getElementsByTagName('tbody')[0].getElementsByTagName('tr');
function showRowsAudio(startIndex) {
  for (var i = 0; i < audiodata.length; i++) {
    audiodata[i].style.display = 'none';
  }
  for (var i = startIndex; i < startIndex + itemsPerPage && i < audiodata.length; i++) {
    audiodata[i].style.display = 'table-row';
  }
}

function updateAudioPaginationButtons() {
  var totalPages = Math.ceil(audiodata.length / itemsPerPage);
  var paginationContainer = document.getElementById("paginationaudio");
  paginationContainer.innerHTML = '';

  if (totalPages >= maxVisiblePages) {
    var startPage = Math.max(1, Math.min(totalPages - maxVisiblePages + 1, Math.ceil(currentIndex / itemsPerPage) - Math.floor(maxVisiblePages / 2) + 1));
    var backedpage = Math.max(1, Math.min(totalPages - maxVisiblePages + 1, Math.ceil(currentIndex / itemsPerPage) - Math.floor(maxVisiblePages / 4) + 1));
    var endPage = Math.min(totalPages, backedpage + maxVisiblePages - 1);
    
    if(startPage >= "3"){
      var firstbutton = document.createElement("button");
      firstbutton.innerHTML = "1";
      firstbutton.addEventListener("click", function() {
      currentIndex = (parseInt(this.innerHTML) - 1) * itemsPerPage;
      showRowsAudio(currentIndex);
      updateAudioPaginationButtons()
    });
    paginationContainer.appendChild(firstbutton);
    var ellipsis = document.createElement("button");
      ellipsis.innerHTML = "...";
      ellipsis.classList.add("ellipsis");
      ellipsis.disabled = false;
      paginationContainer.appendChild(ellipsis);
    }

        for (var i = startPage; i <= endPage; i++) {
        var button = document.createElement("button");
        button.innerHTML = i;
        button.addEventListener("click", function() {
          currentIndex = (parseInt(this.innerHTML) - 1) * itemsPerPage;
          showRowsAudio(currentIndex);
      updateAudioPaginationButtons()
        });  
        if (i === Math.ceil((currentIndex + 2) / itemsPerPage)) {
          button.classList.add("active");
        }  
        paginationContainer.appendChild(button);
      }
      
    if (endPage < totalPages) {
      var ellipsis = document.createElement("button");
      ellipsis.innerHTML = "...";
      ellipsis.classList.add("ellipsis");
      ellipsis.disabled = false;
      paginationContainer.appendChild(ellipsis);
    }
    var lastPageButton = document.createElement("button");
    lastPageButton.innerHTML = totalPages;
    lastPageButton.addEventListener("click", function() {
      currentIndex =  Math.floor((audiodata.length - 1) / itemsPerPage) * itemsPerPage;
      showRowsAudio(currentIndex);
      updateAudioPaginationButtons()
    });
    if (endPage !== totalPages) {
      paginationContainer.appendChild(lastPageButton);
    }   
    
    
  }
   else {
    for (var i = 1; i <= totalPages; i++) {
      var button = document.createElement("button");rows
      button.innerHTML = i;
      button.addEventListener("click", function() {
        currentIndex =  Math.floor((audiodata.length - 1) / itemsPerPage) * itemsPerPage;
        showRowsAudio(currentIndex);
      updateAudioPaginationButtons()
      });

      if (i === Math.ceil((currentIndex + 1) / itemsPerPage)) {
        button.classList.add("active");
      }
      paginationContainer.appendChild(button);
    }
  }
}

function nextPageaudio() {
  currentIndex += itemsPerPage;
  if (currentIndex >= audiodata.length) {
    currentIndex = 0; // Wrap around to the first row if reaching the end
  }
  showRowsAudio(currentIndex);
          updateAudioPaginationButtons();
}

function previousPageaudio() {
  currentIndex -= itemsPerPage;
  if (currentIndex < 0) {
    currentIndex = Math.floor((audiodata.length - 1) / itemsPerPage) * itemsPerPage; // Wrap around to the last page
  }
  showRowsAudio(currentIndex);
          updateAudioPaginationButtons();
}
function itemPerPage(count){
  itemsPerPage=parseInt(count);
  showRows(currentIndex);
  updatePaginationButtons();
}

// Initial display
showRows(currentIndex);
updatePaginationButtons();
showRowsvideo(currentIndex)
updatevideoPaginationButtons();
showRowsAudio(currentIndex);
updateAudioPaginationButtons();