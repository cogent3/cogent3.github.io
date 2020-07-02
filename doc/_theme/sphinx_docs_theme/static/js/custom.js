$.when( $( document ).ready(function() {
    $('.side-nav-menu a').each(function() {
        if ($(this).siblings('ul').length > 0) {
            $(this).prepend('<span class="directlink expandable"></span>')
        } else {
            $(this).prepend('<span class="directlink"></span>')
        }
    });

    $('.side-nav-menu ul li.current').addClass("expanded");
    $('.side-nav-menu ul li:not(li.current)').addClass("collapsed");
    $('.side-nav-menu ul li ul:not(li.current>ul)').addClass("collapsed_items");
    
    $('.side-nav-menu ul li.current a').click(function() {
        $(this).parent().siblings().each(function() {
            $(this).removeClass("current");
            $(this).find('ul').each(function() {
                $(this).addClass("collapsed_items");
                $(this).children().each(function() {
                    $(this).removeClass("current");
                })
            })
        })

        $(this).parent().addClass("current");
        
        $(this).parent().toggleClass("expanded");
        $(this).parent().toggleClass("collapsed");
        $(this).siblings('ul').each(function() {
            $(this).toggleClass("collapsed_items");
        })
    })
})
).then(function() {
    $('.side-nav-menu').toggleClass("hidden");
})