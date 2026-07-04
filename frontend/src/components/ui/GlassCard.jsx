import { motion } from "framer-motion";

export default function GlassCard({

icon,

title,

value,

}){

return(

<motion.div

whileHover={{scale:1.04}}

className="rounded-3xl bg-white/5 backdrop-blur-xl border border-white/10 p-8">

<div className="text-violet-400">

{icon}

</div>

<p className="mt-5 text-gray-400">

{title}

</p>

<h2 className="mt-4 text-5xl font-black">

{value}

</h2>

</motion.div>

)

}