# **Human Genome Organization Dataset**

## **Project Objective**

Sift through an abundance of geneology data from the Human Genome Organization. Build a Flask application for querying and returning information from the HUGO dataset. The included Dockerfile containerizes genes_api.py to make it portable. 

**Data Collected From:**

	https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json

**Data Description**

There are essentially two types of data file (excluding the file format type) of hgnc_complete_set and withdraw. The hgnc_complete_set is a set of all approved gene symbol reports found on the GRCh38 reference and the alternative reference loci (see fig. 2 for a list of columns/headings).

Description from : https://www.genenames.org/download/archive/

### **iss_tracker.py Description:**

#### **Dockerfile Description & Instructions**

How to pull and use the Dockerfule from Docker Hub:

	docker pull khanks0217/gene_api:1.0

How to build a new image from Dockerfile:

	docker build -t username/gene_api:1.0

To launch a redis container that automatically saves:

	docker run -d -p 6379:6379 -v $(pwd)/data:/data:rw redis:7 --save 1 1

On one terminal window, build and run the docker.

	python3 genge_api.py

In a different terminal window, run the different routes by following the respective commands.

##### **Flask API Front End:**

The API front end is expose on port 5000 inside the container. Try the following routes:
	$ curl -X POST localhost:5000/data		Loads data into redis.

	$ curl -X GET localhost:5000/data		Return all data from Redis.

	$ curl -X DELETE localhost:5000/data		Delete all data in Redis.

	$ curl -X localhost:5000/genes			Return json-formatted list of all hgnc_ids

	$ curl -X localhost:5000/genes/<hgnc_id>	Return all data associated with <hgnc_id>


**Expected Output, Sample**

Sample Output - python3 sayitaintgenes.py 

	 * Serving Flask app 'sayitaintgenes'
	 * Debug mode: on
	WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
	 * Running on all addresses (0.0.0.0)
	 * Running on http://127.0.0.1:5000
	 * Running on http://129.114.37.130:5000
	Press CTRL+C to quit
	 * Restarting with stat
	 * Debugger is active!
	 * Debugger PIN: 857-985-880

Sample Output - $ curl -X POST localhost:5000/data

	'Data loaded into Redis'

Sample Output - $ curl -X GET localhost:5000/data

		{
	    "_version_": "1761250385492705280",
	    "agr": "HGNC:42782",
	    "date_approved_reserved": "2011-08-18",
	    "date_modified": "2014-11-19",
	    "ensembl_gene_id": "ENSG00000236036",
	    "entrez_id": "100507114",
	    "gene_group": "Long intergenic non-protein coding RNAs",
	    "gene_group_id": "1986",
	    "hgnc_id": "HGNC:42782",
	    "lncipedia": "LINC00445",
	    "location": "13q13.3",
	    "location_sortable": "13q13.3",
	    "locus_group": "non-coding RNA",
	    "locus_type": "RNA, long non-coding",
	    "name": "long intergenic non-protein coding RNA 445",
	    "refseq_accession": "NR_132115",
	    "rna_central_id": "URS00002F8A2B",
	    "status": "Approved",
	    "symbol": "LINC00445",
	    "ucsc_id": "uc058wkh.1",
	    "uuid": "f9844460-7321-4acf-91a8-4de70c5058dd",
	    "vega_id": "OTTHUMG00000016726"
	  },
	  {
	    "_version_": "1761250409780871168",
	    "agr": "HGNC:16350",
	    "date_approved_reserved": "2002-07-22",
	    "date_modified": "2016-10-05",
	    "date_name_changed": "2010-10-27",
	    "date_symbol_changed": "2010-10-27",
	    "ena": "AF458661",
	    "ensembl_gene_id": "ENSG00000213050",
	    "entrez_id": "252956",
	    "hgnc_id": "HGNC:16350",
	    "location": "7q31.2",
	    "location_sortable": "07q31.2",
	    "locus_group": "pseudogene",
	    "locus_type": "pseudogene",
	    "name": "tropomyosin 3 pseudogene 1",
	    "prev_name": "tropomyosin 3-like 2|tropomyosin 3-like 2 pseudogene",
	    "prev_symbol": "TPM3L2",
	    "pseudogene.org": "PGOHUM00000232970",
	    "pubmed_id": "3024106",
	    "refseq_accession": "NG_005722",
	    "status": "Approved",
	    "symbol": "TPM3P1",
	    "uuid": "65f4b6b3-25ce-4fe8-8825-69270192d42e",
	    "vega_id": "OTTHUMG00000033986"
	  },
	  {
	    "_version_": "1761250370747629568",
	    "agr (continued)
	
Sample Output - $ curl -X DELETE localhost:5000/data

	Data deleted from Redis.

Sample Output - $ curl -X localhost:5000/genes

	[
	  "HGNC:42564",
	  "HGNC:5594",
	  "HGNC:30745",
	  "HGNC:29732",
	  "HGNC:53088",
	  "HGNC:2421",
	  "HGNC:42075",
	  "HGNC:42762",
	  "HGNC:38681",
	  "HGNC:14138",
		(continued)

Sample Output - $ curl -X localhost:5000/genes/<hgnc_id>
	
	{
	  "_version_": "1761250381793329153",
	  "agr": "HGNC:5395",
	  "alias_symbol": "IFNGIP1|PYHIN2",
	  "ccds_id": "CCDS58039|CCDS91080|CCDS1180|CCDS91079",
	  "date_approved_reserved": "1993-09-29",
	  "date_modified": "2023-01-20",
	  "date_name_changed": "2016-03-16",
	  "ena": "M63838",
	  "ensembl_gene_id": "ENSG00000163565",
	  "entrez_id": "3428",
	  "gene_group": "Pyrin domain containing|Pyrin and HIN domain family",
	  "gene_group_id": "994|995",
	  "hgnc_id": "HGNC:5395",
	  "iuphar": "objectId:2924",
	  "location": "1q23.1",
	  "location_sortable": "01q23.1",
	  "locus_group": "protein-coding gene",
	  "locus_type": "gene with protein product",
	  "mane_select": "ENST00000295809.12|NM_001376587.1",
	  "mgd_id": "MGI:96428|MGI:96429|MGI:101847|MGI:2138243|MGI:2138302|MGI:2442822|MGI:3041120|MGI:3584522|MGI:3646410|MGI:3695276|MGI:3780953|MGI:3840117",
	  "name": "interferon gamma inducible protein 16",
	  "omim_id": "147586",
	  "pubmed_id": "1526658|7959953",
	  "refseq_accession": "NM_005531",
	  "status": "Approved",
	  "symbol": "IFI16",
	  "ucsc_id": "uc057mgg.1",
	  "uniprot_ids": "Q16666",
	  "uuid": "b148c95d-977a-4df2-917c-dcdfb86a888f",
	  "vega_id": "OTTHUMG00000037108"
	}


