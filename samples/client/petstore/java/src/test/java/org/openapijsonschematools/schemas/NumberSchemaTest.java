package org.openapijsonschematools.schemas;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.math.BigDecimal;

public class NumberSchemaTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testValidateInteger() {
        Number validatedValue = NumberJsonSchema.validate(1, configuration);
        Assert.assertEquals(validatedValue, 1);
    }

    @Test
    public void testValidateLong() {
        Number validatedValue = NumberJsonSchema.validate(1L, configuration);
        Assert.assertEquals(validatedValue, 1L);
    }

    @Test
    public void testValidateFloat() {
        Number validatedValue = NumberJsonSchema.validate(3.14f, configuration);
        Assert.assertEquals(validatedValue, 3.14f);
    }

    @Test
    public void testValidateDouble() {
        Number validatedValue = NumberJsonSchema.validate(3.14d, configuration);
        Assert.assertEquals(validatedValue, 3.14d);
    }

    @Test
    public void testExceptionThrownForInvalidType() {
        Assert.assertThrows(RuntimeException.class, () -> JsonSchema.validate(
                NumberJsonSchema.class, (Void) null, configuration
        ));
    }
}
