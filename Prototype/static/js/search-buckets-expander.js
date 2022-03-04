let searchBucketsExpander = function() {

    $searchBuckets = document.querySelector('.search-buckets');

    if(!$searchBuckets) {
        return;
    }

    $searchBucketsToHide = document.querySelectorAll("ul[data-id=search-buckets-list] li:not(:first-child)");

    let $showHideButton = document.createElement('button');
    $showHideButton.innerText = 'Show more result categories';
    $showHideButton.classList.add('search-results__bucket-button');
    $showHideButton.setAttribute('aria-expanded', false);
    $showHideButton.setAttribute('aria-label', 'Show or hide result categories');
    $showHideButton.hidden = true;
    $searchBuckets.append($showHideButton);


    let ariaControls = ""
    for(let i = 0; i < $searchBucketsToHide.length; i++) {
        let $bucket = $searchBucketsToHide[i];
        let id = `bucket-${i}`
        $bucket.id = id; // Needed for aria-controls
        ariaControls = `${ariaControls}${id} `; 
    }

    $showHideButton.setAttribute('aria-controls', ariaControls);

    $showHideButton.addEventListener('click', function(e) {
        e.preventDefault();
        let ariaExpanded = $showHideButton.getAttribute('aria-expanded') == 'true';
        $showHideButton.setAttribute('aria-expanded', !ariaExpanded);
        let newAriaExpanded = $showHideButton.getAttribute('aria-expanded') == 'true';

        for(let i = 0; i < $searchBucketsToHide.length; i++) {
            let $bucket = $searchBucketsToHide[i];
            $bucket.hidden = !$bucket.hidden;
        }

        if(newAriaExpanded) {
            $showHideButton.innerHTML = 'Hide more result categories';
        }
        else {
            $showHideButton.innerHTML = 'Show more result categories';
        }
    });

    if(window.innerWidth <= 768) {
        $showHideButton.hidden = false;
        for(let i = 0; i < $searchBucketsToHide.length; i++) {
            let $bucket = $searchBucketsToHide[i];
            $bucket.hidden = true;
        }
    }

    window.addEventListener("resize", debounce(() =>{

        if(window.innerWidth <= 768) {
            $showHideButton.hidden = false;
            $showHideButton.setAttribute('aria-expanded', false);
            $showHideButton.innerHTML = 'Show more result categories';
            for(let i = 0; i < $searchBucketsToHide.length; i++) {
                let $bucket = $searchBucketsToHide[i];
                $bucket.hidden = true;
            }
        }
        else {
            $showHideButton.hidden = true;
            $showHideButton.setAttribute('aria-expanded', false);
            $showHideButton.innerHTML = 'Show more result categories';

            for(let i = 0; i < $searchBucketsToHide.length; i++) {
                let $bucket = $searchBucketsToHide[i];
                $bucket.hidden = false;
            }
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