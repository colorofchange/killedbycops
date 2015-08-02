all: static

#copy to static directory
static: us.json fatalencounters.json doj_focus.csv stories.csv
	cp fatalencounters.json ../static/data/fatalencounters.json
	cp us.json ../static/data/us.json
	cp doj_focus.csv ../static/data/doj_focus.csv
	cp stories.csv ../static/data/stories.csv

clean:
	rm -rf -- *.json build

.PHONY: all clean

#copy files from API
fatalencounters.json:
	curl -o fatalencounters.json 'http://127.0.0.1:8000/api/v1/fatalencounters/?format=json&limit=0' 

#and from google spreadsheet
doj_focus.csv:
	curl -o doj_focus.csv 'https://docs.google.com/spreadsheets/d/15pagGIf7Lc0-wE98jhcMB9bliTDvQD31eeVDzKQEOzg/pub?output=csv'

stories.csv:
	curl -o stories.csv 'https://docs.google.com/spreadsheets/d/1OhT2Cc0-9KFBAECTaBgTyBEJQgKokXfaEpbs6GkiRlU/pub?output=csv'

#US Census shapefiles
build/gz_2010_us_050_00_20m.shp: build/gz_2010_us_050_00_20m.zip
	unzip -od $(dir $@) $<
	touch $@

build/gz_2010_us_050_00_20m.zip:
	mkdir -p $(dir $@)
	curl -o $@ http://www2.census.gov/geo/tiger/GENZ2010/gz_2010_us_050_00_20m.zip

build/counties.json: build/gz_2010_us_050_00_20m.shp ACS_12_5YR_B01003.csv
	topojson \
		-o $@ \
		--id-property='STATE+COUNTY,Id2' \
		--external-properties=ACS_12_5YR_B01003.csv \
		--properties='name=Geography,population=+d.properties["Estimate; Total"]' \
		--projection='width = 960, height = 600, d3.geo.albersUsa() \
			.scale(1280) \
			.translate([width / 2, height / 2])' \
		--simplify=.5 \
		--filter=none \
		-- counties=$<

build/states.json: build/counties.json
	topojson-merge \
		-o $@ \
		--in-object=counties \
		--out-object=states \
		--key='d.id.substring(0, 2)' \
		-- $<

us.json: build/states.json
	topojson-merge \
		-o $@ \
		--in-object=states \
		--out-object=nation \
		-- $<