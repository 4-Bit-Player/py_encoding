

# Small encoding package


Features: 
- 
- En-/Decode most basic python types to strings and back!
   - Lists, Dicts, Tuples, Sets, Str, Int, Float, Bools, None, Bytestrings, Types itself
- Any nested combination is supported.
- "Blazingly fast" decoding and fast encoding
- Support for any valid key values for dictionaries of the supported types
- Smaller resulting size than the build in str function\
  (downside: not really readable/editable strings)


Currently known issues:
- 
- When encoding strings or byte-strings the ' " ' char followed by an unescaped '\3' char will lead to errors.
- Custom Types are not supported
- Circular nested structs are not supported


Made in pure python and somehow faster at decoding than literal_eval.


Faster encoding than the uncached build in str() as well. \
Though unfortunately not as fast when its cached.






