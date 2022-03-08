/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./static/js/src/debounce.js":
/*!***********************************!*\
  !*** ./static/js/src/debounce.js ***!
  \***********************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": function() { return /* export default binding */ __WEBPACK_DEFAULT_EXPORT__; }
/* harmony export */ });
/**
 *
 * Invoke a given callback after debounce function
 * hasn't been called for a specified number of milliseconds
 *
 * usage:
 * debounce( call_back, 500 )( ..arg );
 *
 * @param {Function} call_back
 * @param {Number} wait
 * @param {Object} this_argument
 **/
/* harmony default export */ function __WEBPACK_DEFAULT_EXPORT__(call_back, wait, this_argument) {
  var timer = null;
  return function () {
    for (var _len = arguments.length, args = new Array(_len), _key = 0; _key < _len; _key++) {
      args[_key] = arguments[_key];
    }

    var context = this_argument || this;
    window.clearTimeout(timer);
    timer = window.setTimeout(function () {
      timer = null;
      call_back.apply(context, args);
    }, wait);
  };
}

/***/ }),

/***/ "./static/js/src/global-search.js":
/*!****************************************!*\
  !*** ./static/js/src/global-search.js ***!
  \****************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": function() { return /* export default binding */ __WEBPACK_DEFAULT_EXPORT__; }
/* harmony export */ });
/* harmony default export */ function __WEBPACK_DEFAULT_EXPORT__() {
  var $gsFallbackLink = document.querySelector("a[data-id='search-nav-link']");
  var $main = document.querySelector('main');

  if (!$gsFallbackLink) {
    return;
  }

  $gsFallbackLink.outerHTML = "<button aria-expanded=\"false\" aria-controls=\"gs-component\" aria-label=\"Show/hide global search\" type=\"button\" id=\"gs-show-hide\" class=\"global-search__button\">\n        <span class=\"sr-only\">Search</span>\n      </button>";
  var $gsToggleButton = document.querySelector('#gs-show-hide');
  var $globalSearchComponent = document.createElement('div');
  $globalSearchComponent.hidden = true;
  $globalSearchComponent.id = 'gs-component';
  $globalSearchComponent.classList.add('global-search');
  $globalSearchComponent.innerHTML = "<div class=\"global-search__container\">\n        <h1 class=\"global-search__heading\">Search</h1>\n        <form class=\"global-search__form\" action='/search/featured/' method='GET' id='global-search-form'>\n            <label for=\"search_term\" class=\"global-search__label\">\n                <span class=\"sr-only\">Enter search term.</span> For example, naturalisation or medal cards\n            </label>\n            <input type='search' class='global-search__form-search-box' id='search_term' >\n            <input type=\"submit\" value=\"Search\" class=\"global-search__form-submit\">\n        </form>\n        <p class='global-search__paragraph'>Other ways to find things:</p>\n        <ul class='global-search__list'>\n            <li class='global-search__list-item'>Try the <a href='/search'>search page</a> for more options</li>\n            <li class='global-search__list-item'><a href=''>Explore the collection</a> through topics and time periods</li>\n            <li class='global-search__list-item'><a href=''>Discover Insights</a> for unique stories behind our collection.</li>\n        </ul>\n    </div>";
  $main.insertBefore($globalSearchComponent, $main.childNodes[0]); //IE11 compatible prepend

  $gsToggleButton.addEventListener('click', function (e) {
    var ariaExpanded = $gsToggleButton.getAttribute('aria-expanded') == 'true';
    $gsToggleButton.setAttribute('aria-expanded', !ariaExpanded);
    $globalSearchComponent.hidden = !$globalSearchComponent.hidden;
  });
}

/***/ }),

/***/ "./static/js/src/mobile-filter-expander.js":
/*!*************************************************!*\
  !*** ./static/js/src/mobile-filter-expander.js ***!
  \*************************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": function() { return /* export default binding */ __WEBPACK_DEFAULT_EXPORT__; }
/* harmony export */ });
/* harmony import */ var _debounce_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./debounce.js */ "./static/js/src/debounce.js");

/* harmony default export */ function __WEBPACK_DEFAULT_EXPORT__() {
  var $searchGrid = document.querySelector('div[data-id="catalogue-search-grid"]');
  var $searchFilterContainer = document.querySelector('div[data-id="catalogue-search-sidebar"]');
  var $searchForm = document.querySelector('form[data-id="search-form"]');

  if (!$searchFilterContainer || !$searchGrid || !$searchForm) {
    return;
  }

  var $showHideButton = document.createElement('button');
  $showHideButton.innerText = 'Show search filters';
  $showHideButton.classList.add('search-results__filter-button');
  $showHideButton.setAttribute('aria-expanded', false);
  $showHideButton.setAttribute('aria-controls', 'searchFilterContainer');
  $showHideButton.setAttribute('aria-label', 'Show or hide filters');
  $showHideButton.hidden = true;
  $searchForm.insertBefore($showHideButton, $searchGrid);
  $searchFilterContainer.id = 'searchFilterContainer';
  $showHideButton.addEventListener('click', function (e) {
    e.preventDefault();
    var ariaExpanded = $showHideButton.getAttribute('aria-expanded') == 'true';
    $showHideButton.setAttribute('aria-expanded', !ariaExpanded);
    var newAriaExpanded = $showHideButton.getAttribute('aria-expanded') == 'true';
    $searchFilterContainer.hidden = !$searchFilterContainer.hidden;

    if (newAriaExpanded) {
      $showHideButton.innerHTML = 'Hide search filters';
    } else {
      $showHideButton.innerHTML = 'Show search filters';
    }
  });

  if (window.innerWidth <= 1200) {
    $showHideButton.hidden = false;
    $searchFilterContainer.hidden = true;
  }

  window.addEventListener("resize", (0,_debounce_js__WEBPACK_IMPORTED_MODULE_0__["default"])(function () {
    if (window.innerWidth <= 1200) {
      $showHideButton.hidden = false;
      $searchFilterContainer.hidden = true;
      $showHideButton.setAttribute('aria-expanded', false);
    } else {
      $showHideButton.hidden = true;
      $showHideButton.setAttribute('aria-expanded', false);
      $searchFilterContainer.hidden = false;
    }
  }, 200));
}
;

/***/ }),

/***/ "./static/js/src/search-buckets-expander.js":
/*!**************************************************!*\
  !*** ./static/js/src/search-buckets-expander.js ***!
  \**************************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": function() { return /* export default binding */ __WEBPACK_DEFAULT_EXPORT__; }
/* harmony export */ });
/* harmony import */ var _debounce_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./debounce.js */ "./static/js/src/debounce.js");

/* harmony default export */ function __WEBPACK_DEFAULT_EXPORT__() {
  var $searchBuckets = document.querySelector('.search-buckets');

  if (!$searchBuckets) {
    return;
  }

  var $searchBucketsToHide = document.querySelectorAll("ul[data-id=search-buckets-list] li:not([data-current=True])");
  var $showHideButton = document.createElement('button');
  $showHideButton.innerText = 'Show more result categories';
  $showHideButton.classList.add('search-buckets__toggle-button');
  $showHideButton.setAttribute('aria-expanded', false);
  $showHideButton.setAttribute('aria-label', 'Show or hide result categories');
  $showHideButton.hidden = true;
  $searchBuckets.insertBefore($showHideButton, $searchBuckets.childNodes[0]); //IE11 compatible prepend

  var ariaControls = "";

  for (var i = 0; i < $searchBucketsToHide.length; i++) {
    var $bucket = $searchBucketsToHide[i];
    var id = "bucket-".concat(i);
    $bucket.id = id; // Needed for aria-controls

    ariaControls = "".concat(ariaControls).concat(id, " ");
  }

  $showHideButton.setAttribute('aria-controls', ariaControls);
  $showHideButton.addEventListener('click', function (e) {
    e.preventDefault();
    var ariaExpanded = $showHideButton.getAttribute('aria-expanded') == 'true';
    $showHideButton.setAttribute('aria-expanded', !ariaExpanded);
    var newAriaExpanded = $showHideButton.getAttribute('aria-expanded') == 'true';

    for (var _i = 0; _i < $searchBucketsToHide.length; _i++) {
      var _$bucket = $searchBucketsToHide[_i];
      _$bucket.hidden = !_$bucket.hidden;
    }

    if (newAriaExpanded) {
      $showHideButton.innerHTML = 'Hide more result categories';
    } else {
      $showHideButton.innerHTML = 'Show more result categories';
    }
  });

  if (window.innerWidth <= 768) {
    $showHideButton.hidden = false;

    for (var _i2 = 0; _i2 < $searchBucketsToHide.length; _i2++) {
      var _$bucket2 = $searchBucketsToHide[_i2];
      _$bucket2.hidden = true;
    }
  }

  window.addEventListener("resize", (0,_debounce_js__WEBPACK_IMPORTED_MODULE_0__["default"])(function () {
    if (window.innerWidth <= 768) {
      $showHideButton.hidden = false;
      $showHideButton.setAttribute('aria-expanded', false);
      $showHideButton.innerHTML = 'Show more result categories';

      for (var _i3 = 0; _i3 < $searchBucketsToHide.length; _i3++) {
        var _$bucket3 = $searchBucketsToHide[_i3];
        _$bucket3.hidden = true;
      }
    } else {
      $showHideButton.hidden = true;
      $showHideButton.setAttribute('aria-expanded', false);
      $showHideButton.innerHTML = 'Show more result categories';

      for (var _i4 = 0; _i4 < $searchBucketsToHide.length; _i4++) {
        var _$bucket4 = $searchBucketsToHide[_i4];
        _$bucket4.hidden = false;
      }
    }
  }, 200));
}
;

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	!function() {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = function(exports, definition) {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	}();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	!function() {
/******/ 		__webpack_require__.o = function(obj, prop) { return Object.prototype.hasOwnProperty.call(obj, prop); }
/******/ 	}();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	!function() {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = function(exports) {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	}();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
!function() {
/*!*********************************!*\
  !*** ./static/js/src/search.js ***!
  \*********************************/
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _global_search_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./global-search.js */ "./static/js/src/global-search.js");
/* harmony import */ var _mobile_filter_expander_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./mobile-filter-expander.js */ "./static/js/src/mobile-filter-expander.js");
/* harmony import */ var _search_buckets_expander_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./search-buckets-expander.js */ "./static/js/src/search-buckets-expander.js");



(0,_global_search_js__WEBPACK_IMPORTED_MODULE_0__["default"])();
(0,_mobile_filter_expander_js__WEBPACK_IMPORTED_MODULE_1__["default"])();
(0,_search_buckets_expander_js__WEBPACK_IMPORTED_MODULE_2__["default"])();
}();
/******/ })()
;