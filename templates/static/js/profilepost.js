
    function redirectToAnotherPage() {
      window.location.href = '/profileabout';
  }
  function redirectToProfileabout(){
    window.location.href = '/profilepost';

  }
  function redirecttocircle(){
    window.location.href = '/circle';
  }
  function redirectToEditPage(){
    window.location.href = 'Edit.html';

  }

  setInterval(() => {
    d = new Date(); //object of date()
    hr = d.getHours();
    min = d.getMinutes();
    sec = d.getSeconds();
    hr_rotation = 30 * hr + min / 2; //converting current time
    min_rotation = 6 * min;
    sec_rotation = 6 * sec;
  
    hour.style.transform = `rotate(${hr_rotation}deg)`;
    minute.style.transform = `rotate(${min_rotation}deg)`;
    second.style.transform = `rotate(${sec_rotation}deg)`;
  }, 1000);
  
  document.addEventListener('DOMContentLoaded', function () {
    const navbarButton = document.querySelector('.navbar-toggler');
    const overlayMenu = document.querySelector('.overlay-menu');
  
    navbarButton.addEventListener('click', function () {
      document.body.classList.toggle('overlay-open');
    });
  
    overlayMenu.addEventListener('click', function () {
      document.body.classList.remove('overlay-open');
    });
  });
  

  function toggleCommentSection(id) {
    var commentSection = document.getElementById('commentSection'+id);
    
    var comments = document.getElementById('comments'+id);
    
    if (commentSection.style.display === 'none') {
      commentSection.style.display = 'block';
      comments.style.display = 'block';
    } else {
      commentSection.style.display = 'none';
      comments.style.display = 'none';
    }
  }

 








  