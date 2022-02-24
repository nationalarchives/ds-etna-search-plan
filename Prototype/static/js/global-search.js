
let globalSearch = function () {
    let $gsFallbackLink = document.querySelector("#search-nav-link");
    let $main = document.querySelector('main');
    if(!$gsFallbackLink) {
        return;
    }
    
    $gsFallbackLink.outerHTML = `<button aria-expanded="false" aria-controls="gs-component" aria-label="Show/hide global search" type="button" id="gs-show-hide" class="header__global-search-button">
        <span class="sr-only">Search</span>
      </button>`;
    
    $gsToggleButton = document.querySelector('#gs-show-hide');


    let $globalSearchComponent = document.createElement('div');
    $globalSearchComponent.innerHTML = `Hello world`;
    $globalSearchComponent.hidden = true;
    $globalSearchComponent.id = 'gs-component';    

    $main.prepend($globalSearchComponent);

    $gsToggleButton.addEventListener('click', function(e) {
        let ariaExpanded = $gsToggleButton.getAttribute('aria-expanded') == 'true';
        $gsToggleButton.setAttribute('aria-expanded', !ariaExpanded);

        $globalSearchComponent.hidden = !$globalSearchComponent.hidden;
        
        
    })


}();

