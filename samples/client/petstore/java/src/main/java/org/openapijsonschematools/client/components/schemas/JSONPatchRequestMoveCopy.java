package org.openapijsonschematools.client.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.EnumValidator;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.KeywordValidator;
import org.openapijsonschematools.client.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.RequiredValidator;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;

public class JSONPatchRequestMoveCopy {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public static class From extends StringJsonSchema {}
    
    
    public static class Path extends StringJsonSchema {}
    
    
    public static class Op extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            ))),
            new KeywordEntry("enum", new EnumValidator(Set.of(
                "move",
                "copy"
            )))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateString(Op.class, arg, configuration);
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
        public static JSONPatchRequestMoveCopyMap of(Map<String, String> arg, SchemaConfiguration configuration) throws ValidationException {
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
    public class JSONPatchRequestMoveCopyMapInput {
        // empty mapping
    }
    
    
    public static class JSONPatchRequestMoveCopy1 extends JsonSchema {
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
        public static JSONPatchRequestMoveCopyMap validate(Map<String, String> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateMap(JSONPatchRequestMoveCopy1.class, arg, configuration);
        }
    }
}
