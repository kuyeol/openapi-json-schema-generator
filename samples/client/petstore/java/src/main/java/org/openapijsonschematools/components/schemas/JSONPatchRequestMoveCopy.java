package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class JSONPatchRequestMoveCopy {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public class From extends StringJsonSchema {}
    
    
    public class Path extends StringJsonSchema {}
    
    
    public class Op extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            )))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Op.class, arg, configuration);
        }
    }    
    
    public static class JSONPatchRequestMoveCopyMap extends FrozenMap<String, String> {

        JSONPatchRequestMoveCopyMap(FrozenMap<String, String> m) {

            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "from",
            "op",
            "path"
        );
        public static final Set<String> optionalKeys = Set.of();
        public static JSONPatchRequestMoveCopyMap of(Map<String, String> arg, SchemaConfiguration configuration) {

            return JSONPatchRequestMoveCopy1.validate(arg, configuration);
        }
        
        public String from() {

            return get("from");
        }
        
        public String op() {

            return (String) get("op");

        }
        
        public String path() {

            return get("path");
        }
    }    
    
    public class JSONPatchRequestMoveCopy1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("from", From.class),
                new PropertyEntry("path", Path.class),
                new PropertyEntry("op", Op.class)
            ))),
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "from",
                "op",
                "path"
            ))),
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class))
        ));
        protected static JSONPatchRequestMoveCopyMap getMapOutputInstance(FrozenMap<String, String> arg) {

            return new JSONPatchRequestMoveCopyMap(arg);
        }
        public static JSONPatchRequestMoveCopyMap validate(Map<String, String> arg, SchemaConfiguration configuration) {

            return JsonSchema.validate(JSONPatchRequestMoveCopy1.class, arg, configuration);
        }
    }
}
