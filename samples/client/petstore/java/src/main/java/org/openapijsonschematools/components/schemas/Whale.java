package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.BooleanJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class Whale {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class HasBaleen extends BooleanJsonSchema {}
    
    
    public class HasTeeth extends BooleanJsonSchema {}
    
    
    public class ClassName extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            )))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ClassName.class, arg, configuration);
        }
    }    
    
    public static class WhaleMap extends FrozenMap<String, Object> {

        WhaleMap(FrozenMap<String, Object> m) {

            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "className"
        );
        public static final Set<String> optionalKeys = Set.of(
            "hasBaleen",
            "hasTeeth"
        );
        public static WhaleMap of(Map<String, Object> arg, SchemaConfiguration configuration) {

            return Whale1.validate(arg, configuration);
        }
        
        public String className() {

            return (String) get("className");

        }
        
        public boolean hasBaleen() {

            String key = "hasBaleen";
            throwIfKeyNotPresent(key);
            return (boolean) get(key);

        }
        
        public boolean hasTeeth() {

            String key = "hasTeeth";
            throwIfKeyNotPresent(key);
            return (boolean) get(key);

        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public class Whale1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("hasBaleen", HasBaleen.class),
                new PropertyEntry("hasTeeth", HasTeeth.class),
                new PropertyEntry("className", ClassName.class)
            ))),
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "className"
            )))
        ));
        protected static WhaleMap getMapOutputInstance(FrozenMap<String, Object> arg) {

            return new WhaleMap(arg);
        }
        public static WhaleMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {

            return JsonSchema.validate(Whale1.class, arg, configuration);
        }
    }
}
