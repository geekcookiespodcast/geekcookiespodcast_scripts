////////////////////////////////////////////////////////////////////////////////////
//
// send the current page to geekcookiespodcast@gmail.com :
//
// Title = Page Title
// Body  = URL 

// Beatuful version
javascript: var t = encodeURI(document.title);
var u = encodeURI(window.location);
window.open('https://mail.google.com/mail/?view=cm&to=geekcookiespodcast%40gmail.com&fs=1&tf=1&su=' + t + '&body=' + u);

// bookmarlet
javascript:var t=encodeURI(document.title);var u=encodeURI(window.location);window.open('https://mail.google.com/mail/?view=cm&to=geekcookiespodcast%40gmail.com&fs=1&tf=1&su='+t+'&body='+u);

////////////////////////////////////////////////////////////////////////////////////
//
// send the current page to the private bufferapp address, see 
// https://buffer.com/guides/email for yours and command description.
// Put the email where "XXXYOUR EMAIL HEREXXX" is in the bookmarlet.
//
// Title = Page Title
// Body  = @link URL 

// Beatuful version
javascript: var t = encodeURI(document.title);
var u = '@link ' + encodeURI(window.location);
window.open('https://mail.google.com/mail/?view=cm&to=XXXYOUR EMAIL HEREXXX&fs=1&tf=1&su=' + t + '&body=' + u);

// bookmarlet
javascript:var t=encodeURI(document.title);var u='@link '+encodeURI(window.location);window.open('https://mail.google.com/mail/?view=cm&to=XXXYOUR EMAIL HEREXXX&fs=1&tf=1&su='+t+'&body='+u);

////////////////////////////////////////////////////////////////////////////////////
