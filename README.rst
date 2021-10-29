ckanext-scheming_iso19115
=====================================

|
|

**ckanext-scheming_iso19115** provides the iso19115 interface to create geodcat **metadata** and **resources**.

scheming = scheming_datasets scheming_group sheming_organizations

dcat = dcat dcat_rdf_harvester dcat_json_harvester dcat_json_interface structured_data

ckan.plugins = envvars image_view text_view recline_view datastore datapusher terriajs %[dcat]s %[scheming]s scheming_iso19115
# Scheming # module-path:file to schemas being used
scheming.dataset_schemas = ckanext.scheming_iso19115:scheming/iso.yaml
#scheming.organization_schemas = ckanext.scheming_dcat:scheming/dcat_org.json
scheming.presets = ckanext.scheming_iso19115:scheming/presets.json
