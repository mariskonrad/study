var text = require( '@stdlib/datasets-moby-dick' );

var data;
var i;

data = text();
for ( i = 0; i < data.length; i++ ) {
    console.log( 'Character Count: %d', data[ i ].text.length );
}
