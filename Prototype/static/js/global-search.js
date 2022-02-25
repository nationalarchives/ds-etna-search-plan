
let globalSearch = function () {
    let $gsFallbackLink = document.querySelector("#search-nav-link");
    let $main = document.querySelector('main');
    if(!$gsFallbackLink) {
        return;
    }
    
    $gsFallbackLink.outerHTML = `<button aria-expanded="false" aria-controls="gs-component" aria-label="Show/hide global search" type="button" id="gs-show-hide" class="global-search__button">
        <span class="sr-only">Search</span>
      </button>`;
    
    $gsToggleButton = document.querySelector('#gs-show-hide');


    let $globalSearchComponent = document.createElement('div');
    $globalSearchComponent.innerHTML = `

        <div class="global-search__container">
            <h1 class="global-search__heading">Search</h1>
            <form class="global-search__form" action='/search/featured/' method='GET' id='global-search-form'>
                <label for="search_term" class="global-search__label">
                    <span class="sr-only">Enter search term.</span> For example, naturalisation or medal cards
                </label>
                <input type='search' class='global-search__form-search-box' id='search_term' >
                <input type="submit" value="Search" class="global-search__form-submit">
            </form>
            <p class='global-search__paragraph'>Other ways to find things:</p>
            <ul class='global-search__list'>
                <li class='global-search__list-item'>Try the <a href='/search'>search page</a> for more options</li>
                <li class='global-search__list-item'><a href=''>Explore the collection</a> through topics and time periods</li>
                <li class='global-search__list-item'><a href=''>Discover Insights</a> for unique stories behind our collection.</li>
            </ul>
        
        </div>
   
        `;
    $globalSearchComponent.hidden = true;
    $globalSearchComponent.id = 'gs-component';
    $globalSearchComponent.classList.add('global-search');    

    $main.prepend($globalSearchComponent);

    $gsToggleButton.addEventListener('click', function(e) {
        let ariaExpanded = $gsToggleButton.getAttribute('aria-expanded') == 'true';
        $gsToggleButton.setAttribute('aria-expanded', !ariaExpanded);

        $globalSearchComponent.hidden = !$globalSearchComponent.hidden;
        
        
    })


}();

