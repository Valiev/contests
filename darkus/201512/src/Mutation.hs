module Mutation where

import Data.Text (Text, pack)
import Data.Attoparsec.Text (takeTill, Parser, char, decimal, parseOnly)

type MName = Text
type MNum = Integer

data MDataT = MData {
                  mname :: MName,
                  nn :: MNum,
                  nj :: MNum,
                  jn :: MNum,
                  jj :: MNum
              } deriving Show

mdata2normals :: MDataT -> [Double]
mdata2normals (MData _ a b c d) = map (\x -> fromIntegral x / fromIntegral (max' :: Integer)) [a,b,c,d]
  where max' = maximum [a,b,c,d]

parserLine :: Parser MDataT
parserLine = do
  let sep = ':'
  name' <- takeTill (sep == ) <* char sep
  nn'   <- char ' ' *> decimal
  nj'   <- char ' ' *> decimal
  jn'   <- char ' ' *> decimal
  jj'   <- char ' ' *> decimal
  return $ MData name' nn' nj' jn' jj'

parseLine string = parseOnly parserLine $ pack string

parseData :: String -> [MDataT]
parseData raw_string = concat $ map toMData lines'
  where lines' = lines raw_string
        toMData :: String -> [MDataT]
        toMData x = case parseLine x of
                      Left err -> []
                      Right mdata -> [mdata]
