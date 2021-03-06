# Generated from SystemRDL.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SystemRDLParser import SystemRDLParser
else:
    from SystemRDLParser import SystemRDLParser

# This class defines a complete listener for a parse tree produced by SystemRDLParser.
class SystemRDLListener(ParseTreeListener):

    # Enter a parse tree produced by SystemRDLParser#root.
    def enterRoot(self, ctx:SystemRDLParser.RootContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#root.
    def exitRoot(self, ctx:SystemRDLParser.RootContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_definition.
    def enterProperty_definition(self, ctx:SystemRDLParser.Property_definitionContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_definition.
    def exitProperty_definition(self, ctx:SystemRDLParser.Property_definitionContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_body.
    def enterProperty_body(self, ctx:SystemRDLParser.Property_bodyContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_body.
    def exitProperty_body(self, ctx:SystemRDLParser.Property_bodyContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_type.
    def enterProperty_type(self, ctx:SystemRDLParser.Property_typeContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_type.
    def exitProperty_type(self, ctx:SystemRDLParser.Property_typeContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_default.
    def enterProperty_default(self, ctx:SystemRDLParser.Property_defaultContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_default.
    def exitProperty_default(self, ctx:SystemRDLParser.Property_defaultContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_usage.
    def enterProperty_usage(self, ctx:SystemRDLParser.Property_usageContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_usage.
    def exitProperty_usage(self, ctx:SystemRDLParser.Property_usageContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_component.
    def enterProperty_component(self, ctx:SystemRDLParser.Property_componentContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_component.
    def exitProperty_component(self, ctx:SystemRDLParser.Property_componentContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_boolean_type.
    def enterProperty_boolean_type(self, ctx:SystemRDLParser.Property_boolean_typeContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_boolean_type.
    def exitProperty_boolean_type(self, ctx:SystemRDLParser.Property_boolean_typeContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_string_type.
    def enterProperty_string_type(self, ctx:SystemRDLParser.Property_string_typeContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_string_type.
    def exitProperty_string_type(self, ctx:SystemRDLParser.Property_string_typeContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_number_type.
    def enterProperty_number_type(self, ctx:SystemRDLParser.Property_number_typeContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_number_type.
    def exitProperty_number_type(self, ctx:SystemRDLParser.Property_number_typeContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_ref_type.
    def enterProperty_ref_type(self, ctx:SystemRDLParser.Property_ref_typeContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_ref_type.
    def exitProperty_ref_type(self, ctx:SystemRDLParser.Property_ref_typeContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#component_def.
    def enterComponent_def(self, ctx:SystemRDLParser.Component_defContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#component_def.
    def exitComponent_def(self, ctx:SystemRDLParser.Component_defContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#explicit_component_inst.
    def enterExplicit_component_inst(self, ctx:SystemRDLParser.Explicit_component_instContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#explicit_component_inst.
    def exitExplicit_component_inst(self, ctx:SystemRDLParser.Explicit_component_instContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#anonymous_component_inst_elems.
    def enterAnonymous_component_inst_elems(self, ctx:SystemRDLParser.Anonymous_component_inst_elemsContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#anonymous_component_inst_elems.
    def exitAnonymous_component_inst_elems(self, ctx:SystemRDLParser.Anonymous_component_inst_elemsContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#component_inst_elem.
    def enterComponent_inst_elem(self, ctx:SystemRDLParser.Component_inst_elemContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#component_inst_elem.
    def exitComponent_inst_elem(self, ctx:SystemRDLParser.Component_inst_elemContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#array.
    def enterArray(self, ctx:SystemRDLParser.ArrayContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#array.
    def exitArray(self, ctx:SystemRDLParser.ArrayContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#instance_ref.
    def enterInstance_ref(self, ctx:SystemRDLParser.Instance_refContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#instance_ref.
    def exitInstance_ref(self, ctx:SystemRDLParser.Instance_refContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#instance_ref_elem.
    def enterInstance_ref_elem(self, ctx:SystemRDLParser.Instance_ref_elemContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#instance_ref_elem.
    def exitInstance_ref_elem(self, ctx:SystemRDLParser.Instance_ref_elemContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_assign.
    def enterProperty_assign(self, ctx:SystemRDLParser.Property_assignContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_assign.
    def exitProperty_assign(self, ctx:SystemRDLParser.Property_assignContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#default_property_assign.
    def enterDefault_property_assign(self, ctx:SystemRDLParser.Default_property_assignContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#default_property_assign.
    def exitDefault_property_assign(self, ctx:SystemRDLParser.Default_property_assignContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#explicit_property_assign.
    def enterExplicit_property_assign(self, ctx:SystemRDLParser.Explicit_property_assignContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#explicit_property_assign.
    def exitExplicit_property_assign(self, ctx:SystemRDLParser.Explicit_property_assignContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#post_property_assign.
    def enterPost_property_assign(self, ctx:SystemRDLParser.Post_property_assignContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#post_property_assign.
    def exitPost_property_assign(self, ctx:SystemRDLParser.Post_property_assignContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_assign_rhs.
    def enterProperty_assign_rhs(self, ctx:SystemRDLParser.Property_assign_rhsContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_assign_rhs.
    def exitProperty_assign_rhs(self, ctx:SystemRDLParser.Property_assign_rhsContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#concat.
    def enterConcat(self, ctx:SystemRDLParser.ConcatContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#concat.
    def exitConcat(self, ctx:SystemRDLParser.ConcatContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#concat_elem.
    def enterConcat_elem(self, ctx:SystemRDLParser.Concat_elemContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#concat_elem.
    def exitConcat_elem(self, ctx:SystemRDLParser.Concat_elemContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#s_property.
    def enterS_property(self, ctx:SystemRDLParser.S_propertyContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#s_property.
    def exitS_property(self, ctx:SystemRDLParser.S_propertyContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_rvalue_constant.
    def enterProperty_rvalue_constant(self, ctx:SystemRDLParser.Property_rvalue_constantContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_rvalue_constant.
    def exitProperty_rvalue_constant(self, ctx:SystemRDLParser.Property_rvalue_constantContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#property_modifier.
    def enterProperty_modifier(self, ctx:SystemRDLParser.Property_modifierContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#property_modifier.
    def exitProperty_modifier(self, ctx:SystemRDLParser.Property_modifierContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#s_id.
    def enterS_id(self, ctx:SystemRDLParser.S_idContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#s_id.
    def exitS_id(self, ctx:SystemRDLParser.S_idContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#num.
    def enterNum(self, ctx:SystemRDLParser.NumContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#num.
    def exitNum(self, ctx:SystemRDLParser.NumContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#string.
    def enterString(self, ctx:SystemRDLParser.StringContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#string.
    def exitString(self, ctx:SystemRDLParser.StringContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#enum_def.
    def enterEnum_def(self, ctx:SystemRDLParser.Enum_defContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#enum_def.
    def exitEnum_def(self, ctx:SystemRDLParser.Enum_defContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#enum_body.
    def enterEnum_body(self, ctx:SystemRDLParser.Enum_bodyContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#enum_body.
    def exitEnum_body(self, ctx:SystemRDLParser.Enum_bodyContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#enum_entry.
    def enterEnum_entry(self, ctx:SystemRDLParser.Enum_entryContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#enum_entry.
    def exitEnum_entry(self, ctx:SystemRDLParser.Enum_entryContext):
        pass


    # Enter a parse tree produced by SystemRDLParser#enum_property_assign.
    def enterEnum_property_assign(self, ctx:SystemRDLParser.Enum_property_assignContext):
        pass

    # Exit a parse tree produced by SystemRDLParser#enum_property_assign.
    def exitEnum_property_assign(self, ctx:SystemRDLParser.Enum_property_assignContext):
        pass


