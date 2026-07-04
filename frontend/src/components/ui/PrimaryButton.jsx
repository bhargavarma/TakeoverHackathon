import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";

export default function PrimaryButton(){

return(

<motion.button

whileHover={{scale:1.05}}

whileTap={{scale:.96}}

className="rounded-2xl bg-white text-black px-8 py-4 font-bold text-lg flex items-center gap-4">

<Sparkles/>

Run Daily AI Review

</motion.button>

)

}