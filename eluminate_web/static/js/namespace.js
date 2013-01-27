// Function to namespace the modules for the SSOUK app.
// http://proquestcombo.safaribooksonline.com/9781449399115/classical_pattern_number_symble_1mthe_de?sessionid=#X2ludGVybmFsX0ZsYXNoUmVhZGVyP3htbGlkPTk3ODE0NDkzOTkxMTUvb2JqZWN0X2NyZWF0aW9uX3BhdHRlcm5z

var SSOUK = SSOUK || {};

SSOUK.namespace = function (ns_string) {
    var parts = ns_string.split('.'),
    parent = SSOUK,
    i;

    // strip redundant leading global
    if (parts[0] === "SSOUK") {
        parts = parts.slice(1);
    }

    for (i = 0; i < parts.length; i += 1) {
        // create a property if it doesn't exist
        if (typeof parent[parts[i]] === "undefined") {
            parent[parts[i]] = {};
        }
        parent = parent[parts[i]];
    }
    return parent;
};