import streamlit as st
import helper

st.title("Field Emulator")

m = st.number_input("Enter the degree(m) of polynomial:", min_value=2)
c = st.text_input('Enter irreducible polynomial(in coefficient form with highest power coefficient first):')
c = c.split()
# submit = st.radio('submit2',("Yes","No"))
submit = st.checkbox('Check validity')
# submit = st.button("Submit",disabled=True)
if submit:
    obj = helper.myClass(m, c)
    if (len(obj.c) != obj.m + 1) or (obj.c[0] == '0'):
        print("Error! Inputted polynomial is not of degree m")
    else:
        # st.write(obj.reverse(obj.c))
        obj.c = list(map(int, obj.c))
        obj.reverse(obj.c)
        if obj.irreducibility_check():
            st.write("Your polynomial is irreducible over F_2.")

            st.write("Primitive polynomial is:", end=' ')

            # temp = ""
            # for i in range(obj.m, 0, -1):
            #     if obj.c[i] == 1:
            #         temp = temp + "x^" + str(i) + " + "
            #         # st.write("x^",{i}, "+", end='')
            #         # temp2 = 'x^{i} + '
            #         # st.latex(rf'''{temp2}''')
            # temp += str(obj.c[0])


            # st.latex(rf'''{temp}''')

            st.latex(rf'''{obj.print_result(obj.c)}''')

            a = st.text_input("Enter the first polynomial:", max_chars=(2 * obj.m) - 1).split()
            b = st.text_input("Enter the second polynomial:", max_chars=(2 * obj.m) - 1).split()

            a = list(map(int, a))
            b = list(map(int, b))

            a = obj.reverse(a)
            b = obj.reverse(b)

            show_res = False
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                plus = st.button('Addition(+)')
            with col2:
                minus = st.button('Subtraction(-)')
            with col3:
                mult = st.button('Multiply(*)')
            with col4:
                division = st.button('Division(/)')

            res = [0 for i in range(obj.m)]
            # input_a = [0 for i in range(obj.m)]
            # input_b = [0 for i in range(obj.m)]
            if plus:
                input_a = obj.print_result(a)
                input_b = obj.print_result(b)
                st.write("First polynomial is:")
                st.latex(rf'''{input_a}''')
                st.write("Second polynomial is:")
                st.latex(rf'''{input_b}''')
                res = obj.add(a, b)
                show_res = True

            if minus:
                input_a = obj.print_result(a)
                input_b = obj.print_result(b)
                st.write("First polynomial is:")
                st.latex(rf'''{input_a}''')
                st.write("Second polynomial is:")
                st.latex(rf'''{input_b}''')
                res = obj.add(a, b)
                show_res = True

            if mult:
                input_a = obj.print_result(a)
                input_b = obj.print_result(b)
                st.write("First polynomial is:")
                st.latex(rf'''{input_a}''')
                st.write("Second polynomial is:")
                st.latex(rf'''{input_b}''')
                res = obj.multiply(a, b)
                show_res = True
            if division:
                input_a = obj.print_result(a)
                input_b = obj.print_result(b)
                st.write("First polynomial is:")
                st.latex(rf'''{input_a}''')
                st.write("Second polynomial is:")
                st.latex(rf'''{input_b}''')
                if b == [0 for i in range(m)]:
                    st.write("Division by zero is not possible!!!")
                else:
                    cn = [obj.c[i] for i in range(obj.m + 1)]
                    bn = [b[i] for i in range(obj.m)]
                    u, v = obj.gcd(cn, bn)
                    res = obj.multiply(a, v)
                    show_res = True

            # input_a = obj.print_result(a)
            # input_b = obj.print_result(b)
            final_res = obj.print_result(res)

            # st.latex(rf'''1^st polynomial is {input_a}''')
            # st.latex(rf'''2^nd polynomial is {input_b}''')
            if show_res:
                st.write("The result is:")
                st.latex(rf''' {final_res}''')
        else:
            st.write(
                "Your polynomial is not irreducible over F_2. Please try again with some irreducible polynomial...")
