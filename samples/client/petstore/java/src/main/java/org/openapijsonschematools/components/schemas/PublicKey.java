package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class PublicKey {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Key extends StringJsonSchema {}
    
    
    public static class PublicKeyMap extends FrozenMap<String, Object> {

        PublicKeyMap(FrozenMap<String, Object> m) {

            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "key"
        );
        public static PublicKeyMap of(Map<String, Object> arg, SchemaConfiguration configuration) {

            return PublicKey1.validate(arg, configuration);
        }
        
        public String key() {

            String key = "key";
            throwIfKeyNotPresent(key);
            return (String) get(key);

        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public class PublicKey1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
    
        schema that contains a property named key
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("key", Key.class)
            )))
        ));
        protected static PublicKeyMap getMapOutputInstance(FrozenMap<String, Object> arg) {

            return new PublicKeyMap(arg);
        }
        public static PublicKeyMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {

            return JsonSchema.validate(PublicKey1.class, arg, configuration);
        }
    }
}
