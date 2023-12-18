package org.openapijsonschematools.client.components.schemas;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class Capitalization {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class SmallCamel extends StringJsonSchema {}
    
    
    public static class CapitalCamel extends StringJsonSchema {}
    
    
    public static class SmallSnake extends StringJsonSchema {}
    
    
    public static class CapitalSnake extends StringJsonSchema {}
    
    
    public static class SCAETHFlowPoints extends StringJsonSchema {}
    
    
    public static class ATTNAME extends StringJsonSchema {}
    
    
    public static class CapitalizationMap extends FrozenMap<Object> {
        protected CapitalizationMap(FrozenMap<Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "smallCamel",
            "CapitalCamel",
            "small_Snake",
            "Capital_Snake",
            "SCA_ETH_Flow_Points",
            "ATT_NAME"
        );
        public static CapitalizationMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return Capitalization1.getInstance().validate(arg, configuration);
        }
        
        public String smallCamel() {
            String key = "smallCamel";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String CapitalCamel() {
            String key = "CapitalCamel";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String small_Snake() {
            String key = "small_Snake";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String Capital_Snake() {
            String key = "Capital_Snake";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String SCA_ETH_Flow_Points() {
            String key = "SCA_ETH_Flow_Points";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String ATT_NAME() {
            String key = "ATT_NAME";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public static class CapitalizationMapInput {
        // Map<String, Object> because addProps is unset
    }
    
    
    public static class Capitalization1 extends JsonSchema implements MapSchemaValidator<Object, CapitalizationMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static Capitalization1 instance;
    
        protected Capitalization1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("smallCamel", SmallCamel.class),
                    new PropertyEntry("CapitalCamel", CapitalCamel.class),
                    new PropertyEntry("small_Snake", SmallSnake.class),
                    new PropertyEntry("Capital_Snake", CapitalSnake.class),
                    new PropertyEntry("SCA_ETH_Flow_Points", SCAETHFlowPoints.class),
                    new PropertyEntry("ATT_NAME", ATTNAME.class)
                ))
            );
        }
    
        public static Capitalization1 getInstance() {
            if (instance == null) {
                instance = new Capitalization1();
            }
            return instance;
        }
        
        public CapitalizationMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, Object> properties = new LinkedHashMap<>();
            for(Map.Entry<?, ?> entry: arg.entrySet()) {
                String propertyName = (String) entry.getKey();
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                Object value = entry.getValue();
                JsonSchema propertySchema = pathToSchemas.get(propertyPathToItem).entrySet().iterator().next().getKey();
                Object castValue = (Object) propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, castValue);
            }
            FrozenMap<Object> castProperties = new FrozenMap<>(properties);
            return new CapitalizationMap(castProperties);
        }
        
        @Override
        public CapitalizationMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Map<?, ?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof Map) {
                return getNewInstance((Map<?, ?>) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }

}
