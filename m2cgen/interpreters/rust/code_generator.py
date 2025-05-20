from contextlib import contextmanager

from m2cgen.interpreters.code_generator import CLikeCodeGenerator, CodeTemplate


class RustCodeGenerator(CLikeCodeGenerator):

    def __init__(self, indent=4, dtype='f32'):
        assert dtype in ('f32', 'f64')
        super().__init__(indent)
        self.scalar_type = dtype
        self.slice_type = f"&[{dtype}]"
        self.vector_type = f"Vec<{dtype}>"
        self.tpl_var_declaration = CodeTemplate("let {var_name}: {var_type};")
        self.tpl_num_value = CodeTemplate(f"{{value}}_{dtype}")
        self.tpl_num_inf = CodeTemplate(f"{dtype}::INFINITY")
        self.tpl_num_neginf = CodeTemplate(f"{dtype}::NEG_INFINITY")
        self.tpl_if_statement = CodeTemplate("if {if_def} {{")
        self.tpl_return_statement = CodeTemplate("{value}")

    def add_function_def(self, name, args, is_scalar_output):
        func_args = ", ".join([
            f"{n}: {self._get_input_type(is_vector)}"
            for is_vector, n in args])
        return_type = self._get_var_declare_type(not is_scalar_output)
        self.add_code_lines("#[allow(clippy::excessive_precision, clippy::collapsible_else_if)]")
        function_def = f"fn {name}({func_args}) -> {return_type} {{"
        self.add_code_line(function_def)
        self.increase_indent()

    @contextmanager
    def function_definition(self, name, args, is_scalar_output):
        self.add_function_def(name, args, is_scalar_output)
        yield
        self.add_block_termination()

    def vector_init(self, values):
        return (f"vec![{', '.join(values)}]")

    def _get_input_type(self, is_vector):
        return self.slice_type if is_vector else self.scalar_type

    def _get_var_declare_type(self, is_vector):
        return self.vector_type if is_vector else self.scalar_type