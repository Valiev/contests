module Stats where

pValue :: (Integer, Integer, Integer, Integer) -> Double
pValue (a, b, c, d) = fromRational $ fromIntegral up / fromIntegral down where
  up   = ab * ac * bd * cd
  down = abcd * aa * bb * cc * dd
  ab   = factorial (a + b)
  ac   = factorial (a + c)
  bd   = factorial (b + d)
  cd   = factorial (c + d)
  aa   = factorial a
  bb   = factorial b
  cc   = factorial c
  dd   = factorial d
  abcd = factorial (a + b + c + d)
  factorial n = product [2..n]

sigma xs ys = 0.5 * result
  where result = sqrt $ sum $ map (^2) $ zipWith (-) xs ys

-- correspondence xs ys = 1 - sigma xs ys
