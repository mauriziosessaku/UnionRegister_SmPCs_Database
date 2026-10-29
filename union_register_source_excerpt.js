/* -----------------------------------------------------------------------------
 * Example of the Union Register product-page HTML source (trimmed)
 * Product: Kineret (anakinra)
 * URL:  https://ec.europa.eu/health/documents/community-register/html/h203.htm
 * view-source:  the page embeds its data as JavaScript variables, which the
 * pipeline parses from the HTML/JSON source (no scraping of rendered tables).
 * --------------------------------------------------------------------------- */

var exportTitle = "Kineret";

// (A) PRODUCT-LEVEL METADATA  ->  parsed into the drug-identification/ATC fields
var dataSet_product_information = [
 {"type":"name","title":"Product name","value":"Kineret",
   "meta":{"pre":"h","id":"203","status_name":"ACTIVE","status_type":"g"}},
 {"type":"eu_num","title":"EU number","value":"EU/1/02/203","meta":{}},
 {"type":"inn","title":"Active substance","value":"Anakinra","meta":{}},
 {"type":"indication","title":"Indication",
   "value":"Rheumatoid Arthritis (RA) ... COVID-19 ...","meta":{}},
 {"type":"mah","title":"Marketing Authorisation Holder",
   "value":"Swedish Orphan Biovitrum AB (publ)",
   "meta":{"pre":"mh","id":"17479","address":"112 76 Stockholm, Sverige"}},
 {"type":"atc","title":"ATC","value":null,
   "meta":[[{"level":"1","code":"L",   "description":"Antineoplastic and immunomodulating agents"},
            {"level":"2","code":"L04", "description":"Immunosuppressants"},
            {"level":"3","code":"L04A","description":"Immunosuppressants"},
            {"level":"4","code":"L04AC","description":"Interleukin inhibitors"}]]},
 {"type":"ema_links","title":"Links to EMA website","value":null,
   "meta":[{"url":"https://www.ema.europa.eu/en/medicines/human/EPAR/kineret",
            "description":"EMA - Kineret"}]}
];

// (B) REGULATORY-PROCEDURE METADATA  ->  one row per SmPC update; "closed" is the
//     temporal anchor (reference date) used for time-indexing each drug-AE pair
var dataSet_proc = [
 {"id":"4978","closed":"2002-03-12","type":"Centralised - Authorisation",
   "ema_number":"EMEA/H/C/363",
   "decision":{"number":"(2002) 1045","date":"2002-03-08"},
   "oj":{"date":"2002-03-28","number":"77","page":"32","series":"C"}},
 {"id":"5676","closed":"2002-07-10","type":"Centralised - Variation (no change in Commission Decision)",
   "ema_number":"EMEA/H/C/363/I/2","decision":{"number":null,"date":null}},
 {"id":"5560","closed":"2002-07-15","type":"Centralised - Variation",
   "ema_number":"EMEA/H/C/363/I/1","decision":{"number":"(2002) 2732","date":"2002-07-11"},
   "oj":{"date":"2002-07-26","number":"178","page":"4","series":"C"}}
 /* ... further procedure rows ... */
];
