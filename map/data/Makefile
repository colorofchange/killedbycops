all: static

#copy to static directory
static: us.json fatalencounters.json
	cp fatalencounters.json ../static/data/fatalencounters.json
	cp us.json ../static/data/us.json

clean:
	rm -rf -- *.json build

.PHONY: all clean

#copy files from API
fatalencounters.json:
	curl -o fatalencounters.json 'http://localhost:8000/api/v1/fatalencounters/?format=json&limit=0' 

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