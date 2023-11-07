package org.openapijsonschematools.schemas;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class PathToSchemasMap extends LinkedHashMap<List<Object>, LinkedHashMap<Class<?>, Void>> {

    public void update(PathToSchemasMap other) {
        for (Map.Entry<List<Object>, LinkedHashMap<Class<?>, Void>> entry: other.entrySet()) {
            List<Object> pathToItem = entry.getKey();
            LinkedHashMap<Class<?>, Void> otherSchemas = entry.getValue();
            if (containsKey(pathToItem)) {
                get(pathToItem).putAll(otherSchemas);
            } else {
                put(pathToItem, otherSchemas);
            }
        }
    }
}