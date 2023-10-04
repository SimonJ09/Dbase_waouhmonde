// Shorthand for $( document ).ready()
/*$(function() {
   //$('.menu-navigation:last-child').addClass('last-menu');
   console.log($('.menu-navigation:last-child'));
});
*/

jQuery(document).ready(function ($) {
  /*jQuery( "#navbar-toggler" ).click(function() {
      
  });*/
  
  /*$('.js-tilt').tilt({
    glare: true,
    maxGlare: .5,
    axis: x
  })*/
  
  
  let navbar = $('#header-wm')

  let navPos = navbar.offset().top;

  window.addEventListener("scroll", e => {
    let scrollPos = window.scrollY;
    if (scrollPos >= navPos) {
      navbar.addClass('sticky');
    }
    else {
      navbar.removeClass('sticky');
    }
  })

});


/*
  window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
    alert()
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
  

*/
var splide = new Splide('#splideHomeSection', {
  type: 'loop',
  
focus  : '0',
  omitEnd: true,
  perPage: 6,
  perMove: 1,
  autoplay: true,
  autoScroll: {
    speed: 1,
  },
gap: '1rem',
//padding: { left: '0rem', right: '-5rem' },
  breakpoints: {
    767: {
      perPage: 3,

      gap: '3rem',
    },
    991: {
      perPage: 5,
      gap: '3rem',
    },
    567: {
      perPage: 1,
      gap: '0rem',
      fixedWidth: '100px'
    },
    
    367: {
      perPage: 1,
      gap: '5rem',
      fixedWidth: '80px',
      focus: 'center',
    },
  }
});


splide.mount();



var splideTemoignagesSection = new Splide('#splideTemoignagesSection', {
  type: 'loop',
  focus: 'center',
  perPage: 3,
  perMove: 1,
  autoplay: true,
  autoScroll: {
    speed: 1,
  },
  breakpoints: {
    767: {
      perPage: 1,

      gap: '0rem',
    },
    991: {
      perPage: 3,
      gap: '0rem',
    },
    567: {
      perPage: 1,
      gap: '0rem',
    },
    2000: {
      perPage: 3,
      gap: '0rem',
    }
  }
});
splideTemoignagesSection.mount();

var splideRealisations = new Splide('#splideRealisationSection', {
  type: 'fade',
  perPage: 1,
  perMove: 1,
  autoplay: true,
  autoScroll: {
    speed: 1,
  },
});
splideRealisations.mount();

	