st={12,2,3,11,12,2,3}
print(st)

st.update([2,100])
print(st)
st.remove(12)
print(st)

# frozen sets

f= frozenset(st)
# f.update([2,11])
# f.remove(2)