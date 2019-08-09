## fallback story
* out_of_scope
  - action_default_fallback


  
## 
* greet
  - utter_greet
  

## say goodbye
* goodbye
  - utter_goodbye


## people's cost
* cost-app{"app": "APM"}
  - utter_confirm
* people's cost
  - action_peoples_cost
  

  

## infra cost
* cost-app{"app": "APM"}
  - utter_confirm
* infra cost
  - action_infra_cost
  

## app  jan peoples cost
* app jan peoples cost{"app": "APM"}
   - action_Jan_peoples_cost
   
## app  feb peoples cost
* ###### app feb peoples  cost{"app": "APM"}
   - action_feb_peoples_cost
   
## app  march  peoples cost
* app march peoples cost{"app": "APM"}
   - action_Mar_peoples_cost
   
## app  april  peoples cost
* app april peoples cost{"app": "APM"}
   - action_april_peoples_cost
   
   
## app  may  peoples cost
* app may peoples cost{"app": "APM"}
   - action_May_peoples_cost
   
## app  june  peoples cost
* app june peoples cost{"app": "APM"}
   - action_June_peoples_cost
   
## app  july  peoples cost
* app july peoples cost{"app": "APM"}
   - action_July_peoples_cost
   
   
## app  august  peoples cost
* app august peoples cost{"app": "APM"}
   - action_august_peoples_cost
   
## app  september  peoples cost
* app september peoples cost{"app": "APM"}
   - action_sep_peoples_cost
   
   
## app  october peoples  cost
* app october people's cost{"app": "APM"}
   - action_oct_peoples_cost
   
## app  november  peoples cost
* app november people's cost{"app": "APM"}
   - action_nov_peoples_cost
   
## app december peoples  cost
* app december people's cost{"app": "APM"}
   - action_dec_peoples_cost
   
   
## app  jan  infra cost
* app jan infra cost{"app": "APM"}
   - action_jan_infra_cost
   
## app  feb  infra cost
* app feb infra cost{"app": "APM"}
   - action_feb_infra_cost
   
## app  march  infra cost
* app march infra cost{"app": "APM"}
   - action_Mar_infra_cost
   
## app  april infra cost
* app april infra cost{"app": "APM"}
   - action_april_infra_cost
   
   
## app  may  infra cost
* app may infra cost{"app": "APM"}
   - action_May_infra_cost
   
## app  june  infra cost
* app june infra cost{"app": "APM"}
   - action_June_infra_cost
   
## app  july  infra cost
* app july infra cost{"app": "APM"}
   - action_July_infra_cost
   
   
## app  august infra cost
* app august infra cost{"app": "APM"}
   - action_august_infra_cost
   
## app  september  infra cost
* app september infra cost{"app": "APM"}
   - action_sep_infra_cost
   
## app  october  infra cost
* app october infra cost{"app": "APM"}
   - action_oct_infra_cost
   
   
## app  november infra cost
* app november infra cost{"app": "APM"}
   - action_nov_infra_cost
   
## app  december  infra cost
* app december infra cost{"app": "APM"}
   - action_dec_infra_cost
   
   
   
  
  
## both costs
* cost-app{"app": "APM"}
  - utter_confirm
* both costs
  - action_both_costs

## technologies_used_in_app
* technologies_used_in_app{"app": "APM"}
  - action_technologies
* version of technology{"technology": "oracle"} 
  - action_version
* no_of_dbs{"app": "APM"}
  - action_no_of_dbs
* criticality_of_app{"app": "APM"}
  - action_criticality

## access management1
* access management for app{"app": "APM"}
  - action_access_management
* no_of_applications
  - utter_sub_department
* sub_department
  - action_no_of_apps 
* cost-app{"app": "APM"}
  - utter_confirm
* both costs
  - action_both_costs  

## access management2
* access management for app{"app": "APM"}
  - action_access_management
* no_of_applications
  - utter_sub_department
* sub_department
  - action_no_of_apps 
* cost-app{"app": "APM"}
  - utter_confirm
* infra cost
  - action_infra_cost
  
## access management3
* access management for app{"app": "APM"}
  - action_access_management
* no_of_applications
  - utter_sub_department
* sub_department
  - action_no_of_apps 
* cost-app{"app": "APM"}
  - utter_confirm
* people's cost
  - action_peoples_cost
 
## cost-2app-people
* cost-2app{"app1": "APM","app2": "OPM"}
  - utter_confirm
* people's cost
  - action_peoples_cost 
* Releases
  - action_releases
* deploy
  - action_deploy

## cost-2app-infra
* cost-2app{"app1": "APM","app2": "OPM"}
  - utter_confirm
* infra cost
  - action_infra_cost
* Releases
  - action_releases
* deploy
  - action_deploy
  
## cost-2app-both
* cost-2app{"app1": "APM","app2": "OPM"}
  - utter_confirm
* both costs
  - action_both_costs
* Releases
  - action_releases
* deploy
  - action_deploy

## Generated Story -786283695233447987
* cost-app{"app": "APM"}
    - utter_confirm
* infra cost
    - action_infra_cost

## Generated Story -7165059624913154885
* cost-app{"app": "APM"}
    - utter_confirm
* people's cost
    - action_peoples_cost

## Generated Story -2671371246100123789
* technologies_used_in_app{"app": "XYZ"}
    - slot{"app": "XYZ"}
    - action_technologies
    - slot{"app": "XYZ"}
* version of technology{"technology": "oracle"}
    - action_version
    - slot{"app": "XYZ"}
* no_of_dbs
    - action_no_of_dbs
    - slot{"app": "XYZ"}
* criticality_of_app{"app": "XYZ"}
    - slot{"app": "XYZ"}

## Generated Story 6487077989852393518
* technologies_used_in_app{"app": "APM"}
    - slot{"app": "APM"}
    - action_technologies
    - slot{"app": "APM"}
* version of technology{"technology": "oracle"}
    - action_version
    - slot{"app": "APM"}
* no_of_dbs{"app": "APM"}
    - slot{"app": "APM"}
    - action_no_of_dbs
    - slot{"app": "APM"}
* criticality_of_app{"app": "APM"}
    - slot{"app": "APM"}
    - action_criticality
    - slot{"app": "APM"}

##
* criticality_of_app{"app": "APM"}
    - slot{"app": "APM"}
    - action_criticality
    - slot{"app": "APM"}


##
* version of technology{"technology": "oracle"} 
  - action_version

##
* technologies_used_in_app{"app": "APM"}
  - action_technologies
  
##
* version of technology{"technology": "oracle"} 
  - action_version
  
##
* no_of_dbs{"app": "APM"}
  - action_no_of_dbs
  
##
* criticality_of_app{"app": "XYZ"}
    - slot{"app": "XYZ"}
	
##
* access management for app{"app": "APM"}
  - action_access_management
  
##
* no_of_applications
  - utter_sub_department
  
##
* deploy
  - action_deploy
  
## app-owner
* app-owner{"app": "APM"}
  - action_app_owner

## app-product_group
* app-product_group{"app": "APM"}
  - action_app_product_group
  
## app-products
* app-products{"app": "APM"}
  - action_app_products

## app-release_date
* app-release_date{"app": "APM"}
  - action_app_release_date
  

## app-impacted_regions
* app-impacted_regions{"app": "APM"}
  - action_app_impacted_regions

## app-provider
* app-provider{"app": "APM"}
  - action_app_provider

## app-sponsor
* app-sponsor{"app": "APM"}
  - action_app_sponsor

## app-end_date
* app-end_date{"app": "APM"}
  - action_app_end_date

## app-Provider_organization
* app-Provider_organization{"app": "APM"}
  - action_app_Provider_organization
  
## app-Sponsor_organization
* app-Sponsor_organization{"app": "APM"}
  - action_app_sponsor_organization
  

## app-no_of_servers
* app-no_of_servers
  - action_app_no_of_servers
  
## app-server_name
* app-server_name
  - action_app_server_name

## Generated Story -2231473341400302744
* cost-2app{"app1": "APM", "app2": "OPM"}
    - slot{"app1": "APM"}
    - slot{"app2": "OPM"}
    - utter_confirm
* infra cost
    - action_infra_cost
    - slot{"app": null}
* Releases
    - action_releases
* deploy{"app": "APM"}
    - slot{"app": "APM"}
    - action_deploy
    - slot{"app": "APM"}

## app-app_id	
* app-app_id		
  - action_app_app_id

## app_assessment_date
* app_assessment_date
  - action_app_assessment_date
  
## app_owner_status
* app_owner_status	
  - action_app_owner_status
 
## owmer_signoff_date
* owmer_signoff_date	
  - action_owmer_signoff_date

## provider_signoff_date
* provider_signoff_date	
  - action_provider_signoff_date

## sponsor_signoff_date
* sponsor_signoff_date	
  - action_sponsor_signoff_date

## year_of_assessment
* year_of_assessment	
  - action_year_of_assessment
  
## end of version
* end of version{"version": "11g"}
  - action_end_of_version
  
## product cost
* product cost{"product": "oracle","version": "11g"}
  - action_product_cost

## release type
* release type{"app": "APM","release date": "24-3--2019"}
  - action_release_type
  
## app-employee id
* app-employee id{"app": "APM"}
  - action_app_employee_id
  
## app volumes
* app volumes{"app": "APM"}
  - action_app_volumes
  
## reminder schedule
* reminder schedule{"app": "APM"}
  - action_reminder_schedule
  
## app-employee first name
* app-employee first name{"app": "APM"}
  - action_app_employee_first_name
  
## app-employee last name
* app-employee last name{"app": "APM"}
  - action_app_employee_last_name
  
  
## app-employee place name
* app-employee place name{"app": "APM"}
  - action_app_employee_place_name
  
  
## app-employee email
* app-employee email{"app": "APM"}
  - action_app_employee_email
 
## app-employee country
* app-employee country{"app": "APM"}
  - action_app_employee_country  
  
## app-employee city
* app-employee city{"app": "APM"}
  - action_app_employee_city  
  
## app-employee state
* app-employee state{"app": "APM"}
  - action_app_employee_state  
  
## app-employee region
* app-employee region{"app": "APM"}
  - action_app_employee_region
  
## Generated Story -3158807542460308967
* app-Sponsor_organization{"app": "ABC"}
    - slot{"app": "ABC"}
    - action_app_sponsor_organization
    - slot{"app": "ABC"}
* app-Provider_organization{"app": "XYZ"}
    - slot{"app": "XYZ"}
    - action_app_Provider_organization
    - slot{"app": "XYZ"}
* app-end_date{"app": "pl"}
    - slot{"app": "pl"}
    - action_app_end_date
    - slot{"app": "pl"}
* app-sponsor{"app": "bita"}
    - slot{"app": "bita"}
    - action_app_sponsor
    - slot{"app": "bita"}
* app-provider{"app": "RMY"}
    - slot{"app": "RMY"}
    - action_app_provider
    - slot{"app": "RMY"}
* app-impacted_regions{"app": "birma"}
    - slot{"app": "birma"}
    - action_app_impacted_regions
    - slot{"app": "birma"}
* app-release_date
    - action_app_release_date
    - slot{"app": "birma"}
* app-products{"app": "APM"}
    - slot{"app": "APM"}
    - action_app_products
    - slot{"app": "APM"}
* app-owner{"app": "ZMR"}
    - slot{"app": "ZMR"}
    - action_app_owner
    - slot{"app": "ZMR"}

## Generated Story 7544570764624902501
* app-owner{"app": "APM"}
    - slot{"app": "APM"}
    - action_app_owner
    - slot{"app": "APM"}
* app-Provider_organization{"app": "pl"}
    - slot{"app": "pl"}
    - action_app_Provider_organization
    - slot{"app": "pl"}
* app-end_date{"app": "pl"}
    - slot{"app": "pl"}
    - action_app_end_date
    - slot{"app": "pl"}
* app-impacted_regions{"app": "vita"}
    - slot{"app": "vita"}
    - action_app_impacted_regions
    - slot{"app": "vita"}
* app-product_group{"app": "XYZ"}
    - slot{"app": "XYZ"}
    - action_app_product_group
    - slot{"app": "XYZ"}
* app-provider{"app": "ZMA"}
    - slot{"app": "ZMA"}
    - action_app_provider
    - slot{"app": "ZMA"}
* app-release_date{"app": "DJA"}
    - slot{"app": "DJA"}
    - action_app_release_date
    - slot{"app": "DJA"}
* app-sponsor{"app": "APM"}
    - slot{"app": "APM"}
    - action_app_sponsor
    - slot{"app": "APM"}
* cost-app
    - utter_confirm
* both costs
    - action_both_costs
    - slot{"app": "APM"}

## Generated Story 4205823055386847418
* year_of_assessment{"app": "APM"}
    - slot{"app": "APM"}
    - action_year_of_assessment
    - slot{"app": "APM"}
* sponsor_signoff_date{"app": "APM"}
    - slot{"app": "APM"}
    - action_sponsor_signoff_date
    - slot{"app": "APM"}
* provider_signoff_date{"app": "POM"}
    - slot{"app": "POM"}
    - action_provider_signoff_date
    - slot{"app": "POM"}
* owmer_signoff_date
    - action_owmer_signoff_date
    - slot{"app": "POM"}
* app_owner_status{"app": "POM"}
    - slot{"app": "POM"}
    - action_app_owner_status
    - slot{"app": "POM"}
* app_assessment_date{"app": "pl"}
    - slot{"app": "pl"}
    - action_app_assessment_date
    - slot{"app": "pl"}
* app-app_id{"app": "pl"}
    - slot{"app": "pl"}
    - action_app_app_id
    - slot{"app": "pl"}


## app-provider signoff
* app-provider signoff{"app": "ABC"} 
  - action_app_provider_signoff
  
## app-aseessment status
* app-aseessment status{"app": "ABC"}
  - action_app_aseessment_status
 
## app-sponsor signoff
* app-sponsor signoff{"app": "ABC"} 
  - action_app_sponsor_signoff
 
## app-Basel 1 regulatory
* app-Basel 1 regulatory{"app": "ABC"} 
  - action_app_Basel1_regulatory
 
## app-Basel 2 regulatory
* app-Basel 2 regulatory{"app": "ABC"}
  - action_app_basel2_regulatory
 
## app-Basel 3 regulatory
* app-Basel 3 regulatory{"app": "ABC"}
  - action_app_basel3_regulatory
 
## app-APAC regulatory
* app-APAC regulatory{"app": "ABC"}
  - action_app_APAC_regulatory
 
## app-Business criticality
* app-Business criticality{"app": "ABC"} 
  - action_app_Business_criticality