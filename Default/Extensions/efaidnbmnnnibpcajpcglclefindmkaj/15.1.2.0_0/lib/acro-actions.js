/*************************************************************************
* ADOBE CONFIDENTIAL
* ___________________
*
*  Copyright 2015 Adobe Systems Incorporated
*  All Rights Reserved.
*
* NOTICE:  All information contained herein is, and remains
* the property of Adobe Systems Incorporated and its suppliers,
* if any.  The intellectual and technical concepts contained
* herein are proprietary to Adobe Systems Incorporated and its
* suppliers and are protected by all applicable intellectual property laws,
* including trade secret and or copyright laws.
* Dissemination of this information or reproduction of this material
* is strictly forbidden unless prior written permission is obtained
* from Adobe Systems Incorporated.
**************************************************************************/
function dependOn(){"use strict";return[require("communicate"),require("common"),require("util"),require("proxy"),require("analytics"),require("acro-web2pdf")]}var def;require=function(e){"use strict";return e},def=window.define?window.define:function(e,n){"use strict";return n.apply(null,[{ajax:$.ajax.bind($)}])};var exports=acom_analytics={};def(dependOn(),(function(e,n,t,o,r,i){"use strict";var s,a=null;for(s in a||(a=new function(){this.proxy=o.proxy.bind(this),this.LOG=n.LOG,this.getVersion=function(n){var t,o=function(o){o&&(clearTimeout(t),o.fillnSignEnabled&&"true"===o.fillnSignEnabled?SETTINGS.FILL_N_SIGN_ENABLED=!0:SETTINGS.FILL_N_SIGN_ENABLED=!1,o.frictionlessEnabled&&"false"===o.frictionlessEnabled&&(SETTINGS.FRICTIONLESS_ENABLED=!1),o.optinState&&"false"===o.optinState?SETTINGS.ANALYTICS_OPT_IN=!1:1==+o.majorVersion?(r.event(r.e.SHIM_VERSION,{VERSION:"Unknown"}),r.shim="unknown"):0==+o.majorVersion?(r.event(r.e.SHIM_VERSION,{VERSION:"None"}),r.shim="none"):(r.event(r.e.SHIM_VERSION,{VERSION:o.majorVersion+"."+o.minorVersion}),r.shim=o.majorVersion+"."+o.minorVersion),e.setVersion(+o.majorVersion),n(+o.majorVersion))};t=setTimeout((function(){o({messageType:"shimVersionInfo",majorVersion:"1",minorVersion:"0"})}),2e3),i.getVersion(o)},this.openInAcrobat=function(n){var o=this;chrome.tabs.get(n.tabId,(function(r){if(r.url&&(n.url=r.url),void 0===n.filename&&(n.filename=e.filenameFromUrl(n.url)),e.version>1){if(n.authenticatedPDF&&1==n.authenticatedPDF)return delete n.authenticatedPDF,"pdf_downloaded"===n.current_status&&n.base64PDF&&i.openInAcrobat(n),void e.sendMessage(n);n.panel_op="status",n.current_status="pdf_downloading",e.sendMessage(n);var s=t.newXHR();s.open("GET",n.url,!0),s.responseType="blob",s.onload=o.proxy((function(t){var o;s.status<400?"application/pdf"===s.response.type?((o=new FileReader).onloadend=function(t){n.base64PDF=t.target.result,i.openInAcrobat(n),n.content_op="status",n.current_status="pdf_downloaded",e.sendMessage({tabId:n.tabId,loaded:n.loaded,filename:n.filename,url:n.url,persist:n.persist,version:n.version,start:n.start,is_pdf:n.is_pdf,newUI:n.newUI,panel_op:n.panel_op,content_op:n.content_op,current_status:"pdf_downloaded"})},o.readAsDataURL(s.response)):(n.authenticatedPDF=!0,e.sendMessage(n)):(n.panel_op="status",n.current_status="pdf_failure",e.sendMessage(n))})),s.send()}else chrome.downloads.download({url:n.url,conflictAction:"uniquify"})}))},this.open_converted_file=function(e){i.openFile(e)}}),a)a.hasOwnProperty(s)&&("function"==typeof a[s]?exports[s]=a[s].bind(a):exports[s]=a[s]);return e.registerHandlers({open_in_acrobat:a.proxy(a.openInAcrobat),open_converted_file:a.proxy(a.open_converted_file)}),a}));