

function test_inrange(){
	    var teststr = String($("#glu_ac").text().trim());
        var testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 111 || testval < 59)?($("#glu_ac").attr("class","table-danger")):($("#glu_ac").attr("class","table-secondary"));

        teststr = String($("#ast").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 30 || testval < 10)?($("#ast").attr("class","table-danger")):($("#ast").attr("class","table-secondary"));

        teststr = String($("#alt").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 32 || testval < 2)?($("#alt").attr("class","table-danger")):($("#alt").attr("class","table-secondary"));

        teststr = String($("#cho").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 200 || testval < 110)?($("#cho").attr("class","table-danger")):($("#cho").attr("class","table-secondary"));

        teststr = String($("#tg").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 180 || testval < 35)?($("#tg").attr("class","table-danger")):($("#tg").attr("class","table-secondary")); 

        teststr = String($("#hdl").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 80 || testval < 27)?($("#hdl").attr("class","table-danger")):($("#hdl").attr("class","table-secondary"));

        teststr = String($("#bun").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 24 || testval < 6)?($("#bun").attr("class","table-danger")):($("#bun").attr("class","table-secondary"));

        teststr = String($("#cre").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 1.4 || testval < 0.5)?($("#cre").attr("class","table-danger")):($("#cre").attr("class","table-secondary"));

        teststr = String($("#ua").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 7.2 || testval < 2.4)?($("#ua").attr("class","table-danger")):($("#ua").attr("class","table-secondary"));

        teststr = String($("#ca").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 10.6 || testval < 8.8)?($("#ca").attr("class","table-danger")):($("#ca").attr("class","table-secondary"));

        teststr = String($("#ldh").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 180 || testval < 91)?($("#ldh").attr("class","table-danger")):($("#ldh").attr("class","table-secondary"));

        teststr = String($("#ck").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 167 || testval < 13)?($("#ck").attr("class","table-danger")):($("#ck").attr("class","table-secondary"));

        teststr = String($("#amy").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 115 || testval < 25)?($("#amy").attr("class","table-danger")):($("#amy").attr("class","table-secondary"));

        teststr = String($("#na").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 145 || testval < 135)?($("#na").attr("class","table-danger")):($("#na").attr("class","table-secondary"));

        teststr = String($("#k").text().trim());
        testval = Number(teststr.slice(teststr.indexOf(' ') +1,));
        (testval > 5 || testval < 3.6)?($("#k").attr("class","table-danger")):($("#k").attr("class","table-secondary"));
}