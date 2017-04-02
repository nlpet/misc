def get_output_shape(inpts, fs, s, p, k):
    """Calculates the output shape of a convolution

    :inpts input shape (h, w, d)
    :fs filter shape (h, w, d )
    :s stride (h, w)
    :p padding (h, w)
    :k number of filters
    """
    new_height = (inpts[0] - fs[0] + 2 * p[0]) / s[0] + 1
    new_width = (inpts[1] - fs[1] + 2 * p[1]) / s[1] + 1
    return (new_height, new_width, k)
