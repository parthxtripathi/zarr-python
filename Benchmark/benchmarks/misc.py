import zarr
import numpy as np
import time
from tempfile import TemporaryDirectory

class misc():
    def time_misc(self):
        """
        Measure the time required and number of objects created when writing
        to a Zarr array with random ints or fill value.
        """
        chunks = (8192,)
        shape = (chunks[0] * 1024,)
        data = np.random.randint(0, 255, shape)
        dtype = 'uint8'

        with TemporaryDirectory() as store:
            arr = zarr.open(store,
            shape=shape,
            chunks=chunks,
            dtype=dtype,
            write_empty_chunks=True,
            fill_value=0,
            mode='w')
            # initialize all chunks
        arr[:] = 100
        result = []
        for value in (data, arr.fill_value):
            start = time.time()
            arr[:] = value
            elapsed = time.time() - start
            result.append((elapsed, arr.nchunks_initialized))

        return result
