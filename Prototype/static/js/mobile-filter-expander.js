let mobileFilterExpander = function() {
    let $searchFilterContainer = document.querySelector('.catalogue-search-grid__sidebar');

    let $searchGrid = document.querySelector('.catalogue-search-grid');
    let $searchForm = document.querySelector('.search-form');

    if(!$searchFilterContainer || !$searchGrid || !$searchForm) {
        return;
    }



    let $showHideButton = document.createElement('button');
    $showHideButton.innerText = 'Show or hide filters';
    $showHideButton.classList.add('search-results__filter-button');
    $showHideButton.setAttribute('aria-expanded', false);
    $showHideButton.setAttribute('aria-controls', 'searchFilterContainer');
    $showHideButton.setAttribute('aria-label', 'Show/hide filters');
    $showHideButton.hidden = true;
    $searchForm.insertBefore($showHideButton, $searchGrid);

    $searchFilterContainer.id = 'searchFilterContainer';

    $showHideButton.addEventListener('click', function(e) {
        e.preventDefault();
        let ariaExpanded = $showHideButton.getAttribute('aria-expanded') == 'true';
        $showHideButton.setAttribute('aria-expanded', !ariaExpanded);

        $searchFilterContainer.hidden = !$searchFilterContainer.hidden;
        
        
    });


    if(window.innerWidth <= 1200) {
        $showHideButton.hidden = false;
        $searchFilterContainer.hidden = true;
    }

    window.addEventListener("resize", debounce(() =>{

        if(window.innerWidth <= 1200) {
            $showHideButton.hidden = false;
            $searchFilterContainer.hidden = true;
            $showHideButton.setAttribute('aria-expanded', false);
        }
        else {
            $showHideButton.hidden = true;
            $showHideButton.setAttribute('aria-expanded', false);
            $searchFilterContainer.hidden = false;
        }
    
    }, 200));

}();

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

 function debounce(call_back, wait, this_argument) {

    var timer = null;

    return function (...args) {

        var context = this_argument || this;

        window.clearTimeout(timer);

        timer = window.setTimeout(() => {

            timer = null;

            call_back.apply(context, args);

        }, wait);
    };
}