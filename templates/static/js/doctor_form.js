function validateForm() {
    var firstName = document.getElementById('First_Name');
    var lastName = document.getElementById('Last_Name');
    var genderName = document.getElementById('Gender');
    var dobName = document.getElementById('dob');
    var phoneName = document.getElementById('phone');
    var emailName = document.getElementById('email');
    var specialistName = document.getElementById('specialist');
    var countryName = document.getElementById('country');
    var addressName = document.getElementById('address');
    var stateName = document.getElementById('state');
    var experienceName = document.getElementById('experience');
    var certificateName = document.getElementById('certificate');
    var profilePhotoName = document.getElementById('profilePhoto');

    var firstNameError = document.getElementById('firstNameError');
    var lastNameError = document.getElementById('lastNameError');
    var genderNameError = document.getElementById('genderNameError');
    var selectedGender = genderName.options[genderName.selectedIndex].value;
    var dobNameError = document.getElementById('dobNameError');
    var phoneNameError = document.getElementById('phoneNameError');
    var emailNameError = document.getElementById('emailNameError');
    var specialistNameError = document.getElementById('specialistNameError');
    var countryNameError = document.getElementById('countryNameError');
    var addressNameError = document.getElementById('addressNameError');
    var stateNameError = document.getElementById('stateNameError');
    var experienceNameError = document.getElementById('experienceNameError');
    var certificateNameError = document.getElementById('certificateNameError');        
    var profilePhotoNameError = document.getElementById('profilePhotoNameError');


    firstNameError.textContent = '';
    lastNameError.textContent = '';
    genderNameError.textContent = '';
    dobNameError.textContent = '';
    phoneNameError.textContent = '';
    emailNameError.textContent = '';
    specialistNameError.textContent = '';
    countryNameError.textContent = '';
    addressNameError.textContent = '';
    stateNameError.textContent = '';
    experienceNameError.textContent = '';
    certificateNameError.textContent = '';
    profilePhotoNameError.textContent = '';

    if (firstName.value.trim() === '') {
      firstNameError.textContent = 'Please enter your First Name';
      firstName.focus(); 
      return false;
    }
    if (lastName.value.trim() === '') {
      lastNameError.textContent = 'Please enter your Last Name';
      lastName.focus(); 
      return false;
    }
    if (selectedGender.trim() === '') {
      genderNameError.textContent = 'Please select your Gender';
      genderName.focus(); 
      return false;
    }
    if (dobName.value.trim() === '') {
      dobNameError.textContent = 'Please enter your Date of Birth';
      dobName.focus();
      return false;
    }
    if (phoneName.value.trim() === '') {
      phoneNameError.textContent = 'Please enter your Phone Number';
      phoneName.focus();
      return false;
    } else if (!/^\d{10}$/.test(phoneName.value.trim())) {
      phoneNameError.textContent = 'Please enter a valid 10-digit Phone Number';
      phoneName.focus();
      return false;
    }
    if (emailName.value.trim() === '') {
      emailNameError.textContent = 'Please enter your Email';
      emailName.focus();
      return false;
    } else {
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailName.value.trim())) {
        emailNameError.textContent = 'Please enter a valid Email address';
        emailName.focus();
        return false;
      }
    }
    if (specialistName.value.trim() === '') {
      specialistNameError.textContent = 'Please enter your specialist Name';
      specialistName.focus(); 
      return false;
    }
    if (countryName.value.trim() === '') {
      countryNameError.textContent = 'Please enter your country Name';
      countryName.focus(); 
      return false;
    }
    if (addressName.value.trim() === '') {
      addressNameError.textContent = 'Please enter your address Name';
      addressName.focus(); 
      return false;
    }
    if (stateName.value.trim() === '') {
      stateNameError.textContent = 'Please enter your state Name';
      stateName.focus(); 
      return false;
    }
    if (experienceName.value.trim() === '') {
        experienceNameError.textContent = 'Please enter your Years of Experience';
        experienceName.focus(); 
      return false;
    }

    if (certificateName.value.trim() === '') {
      certificateNameError.textContent = 'Please upload your certificate';
      certificateName.focus(); 
      return false;
    }
    if (profilePhotoName.value.trim() === '') {
      profilePhotoNameError.textContent = 'Please upload your Profile Photo';
      profilePhotoName.focus();
      return false;
    }
    return true;
  }