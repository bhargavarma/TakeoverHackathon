import PrimaryButton from "../ui/PrimaryButton";

export default function Hero() {
  return (
    <div className="relative overflow-hidden rounded-[36px] bg-gradient-to-br from-violet-700 via-indigo-600 to-cyan-500 p-12">

      <div className="absolute right-[-120px] top-[-120px] h-96 w-96 rounded-full bg-white/10 blur-3xl"/>

      <div className="absolute bottom-[-120px] left-[-120px] h-96 w-96 rounded-full bg-cyan-300/20 blur-3xl"/>

      <span className="rounded-full bg-white/20 px-5 py-2 text-sm font-semibold">

        🤖 AI COO ACTIVE

      </span>

      <h1 className="mt-6 text-6xl font-black leading-tight">

        Autonomous

        <br/>

        Business Operations

      </h1>

      <p className="mt-6 max-w-2xl text-lg opacity-90">

        AI continuously monitors inventory,

        generates purchase orders,

        sends executive reports,

        and keeps your business running.

      </p>

      <div className="mt-10">

        <PrimaryButton/>

      </div>

    </div>
  );
}