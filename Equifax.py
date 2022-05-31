package com.equifax.config;

import org.apache.beam.sdk.options.Default;
import org.apache.beam.sdk.options.Description;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.Validation;

public interface PFAPreprocessingOptions extends PipelineOptions {

    @Validation.Required
    @Description("Key Vault URL, for example: https://vault-uat.us.equifax.com")
    String getVaultUrl();

    void setVaultUrl(String value);

    @Validation.Required
    @Description("Key Vault Namespace, for example: csa-edh/edh1-npe")
    String getVaultNamespace();

    void setVaultNamespace(String value);

    @Validation.Required
    @Description("URL of the Vault server instance")
    String getVaultAddress();

    void setVaultAddress(String var1);

    @Description("Oracle Key Vault path, for example: cda/db/airflow/us-east1/dev-oracle")
    String getVaultOraclePath();

    void setVaultOraclePath(String value);

    @Description("MongoDb Key Vault path, for example: cda/db/airflow/us-east1/dev-oracle")
    String getVaultMongoDbPath();

    void setVaultMongoDbPath(String value);

    @Description("MongoDb Decryption Keys Vault path, for example: cda/db/airflow/us-east1/dev-oracle")
    String getVaultMongoKeysPath();

    void setVaultMongoKeysPath(String value);

    @Validation.Required
    @Description("DSG API Secrets Vault path, for example: cda/db/airflow/us-east1/dev-decrypt-dsg-api")
    String getVaultDSGSecretsPath();

    void setVaultDSGSecretsPath(String value);

    @Validation.Required
    @Description("Service account used to sign JWT token")
    String getVaultServiceAccount();

    void setVaultServiceAccount(String value);

    @Validation.Required
    @Description("Role, used to sign JWT token and authenticate in Vault")
    String getVaultRole();

    void setVaultRole(String value);

//    The following parameters are required in case SSL is used
//
//    @Description("GCS path to vault keyStore")
//    String getVaultKeyStorePath();
//
//    void setVaultKeyStorePath(String path);
//
//    @Default.String("changeit")
//    @Description("Password to vault keyStore")
//    String getVaultKeyStorePassword();
//
//    void setVaultKeyStorePassword(String password);
//
//    @Default.String("PKCS12")
//    @Description("Type of the KeyStore (i.e. JKS or PKCS12")
//    String getVaultKeyStoreType();
//
//    void setVaultKeyStoreType(String type);

    @Default.Integer(2)
    @Description("Vault engine version")
    int getEngineVersion();

    void setEngineVersion(int version);

    @Validation.Required
    @Description("Service Account")
    String getServiceAccount();

    void setServiceAccount(String value);

    @Description("Source DB time zone. Using this timezone, all timestamps will be converted to UTC and stored as strings.")
    @Default.String("UTC")
    String getTimeZone();

    void setTimeZone(String zone);

    @Description("Tenant Code")
    String getTenantCode();

    void setTenantCode(String value);

    @Description("Partner Code")
    String getPartnerCode();

    void setPartnerCode(String value);

    @Description("Config Code")
    String getConfigCode();

    void setConfigCode(String value);

    @Description("Equifax Channel")
    String getEquifaxChannel();

    void setEquifaxChannel(String value);

    @Description("Experian Channel")
    String getExperianChannel();

    void setExperianChannel(String value);

    @Description("Transunion Channel")
    String getTransunionChannel();

    void setTransunionChannel(String value);

//    @Description("Collection name to Mongo DB")
//    @Validation.Required
//    String getCollectionName();
//
//    void setCollectionName(String value);

    @Description("Type of date column for filtering. 'String' by default.")
    @Default.String("String")
    String getDateType();

    void setDateType(String value);

    @Description("Pattern to parse datetime fields. " +
            "Default value is taken from 'pet' database, 'customerInformation' collection, e.g. '2018/06/12 17:55:53 UTC'")
    @Default.String("yyyy/MM/dd HH:mm:ss z")
    String getDateTimeFieldsPattern();

    void setDateTimeFieldsPattern(String value);

    @Description(
            "This field (in conjunction with fromDate and toDate) is used to set the date range for the records to be read from DB. " +
                    "Should conform to the pattern specified in 'dateTimeFieldsPattern'")
    String getDateFilterField();

    void setDateFilterField(String value);

    @Description("Left bound of the date range for the records to be read from DB")
    String getFromDate();

    void setFromDate(String value);

    @Description("Right bound of the date range for the records to be read from DB")
    String getToDate();

    void setToDate(String value);

//    @Description("Filter field name")
//    String getFilterFieldName();
//
//    void setFilterFieldName(String value);

    @Description("Filter field value")
  
    String getFilterFieldValue();
//   string Username = "16200";
//   string passwd = "dEbdv7Q82sz54zc2t7";
//            string service_name = "acroxml";
//            string eqresponse;
//            string CustomerCode = "ISTS";
//            string SecurityCode = "C53";
//            string CustomerNumber = "402FA16729";
//            string eqxmlstr;
  
// Example POST String XML_URL ...
            string url;
            url = "https://transport5.ec.equifax.com/ists/stspost?require_security=";
  
  
    void setFilterFieldValue(String value);

//    @Description("Set to false if Aggregates based query should be used. Else Filter based query will be used")
//    @Default.String("true")
//    String getUseFilterQuery();
//
//    void setUseFilterQuery(String value);

//    @Description("Set to false if _id filed is represented as ObjectID. Else _id filed is assumed to be UUID " +
//            "string")
//    @Default.String("true")
//    String getObjectIdAsUUID();
//
//    void setObjectIdAsUUID(String value);

    @Description("Artifacts bucket name, for example: gcs-cda-us-edh1-npe-artifacts")
    String getArtifactsBucketName();

    void setArtifactsBucketName(String value);

    @Description("Output Files root Path to store result preprocessing alert records")
    @Default.String("gs://us-gcs-gbp-batch/dev/input")
    String getOutputFileRootPath();

    void setOutputFileRootPath(String value);


    @Description("The start date. Expected formats 'yyyy-MM-dd', 'yyyy-MM-dd-HHmmss'.")
    String getStartDate();

    void setStartDate(String value);

    @Description("The end date. Expected formats 'yyyy-MM-dd', 'yyyy-MM-dd-HHmmss'.")
    String getEndDate();

    void setEndDate(String value);

}
